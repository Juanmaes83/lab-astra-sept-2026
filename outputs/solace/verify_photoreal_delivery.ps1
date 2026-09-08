$ErrorActionPreference = 'Stop'
$solaceBase = $PSScriptRoot
$solaceFrames = Join-Path $solaceBase 'photoreal-work/final-frames-r2'
$solaceMovie = Join-Path $solaceBase 'SOLACE_PHOTOREAL_GOAL_v01.mp4'
$solaceBlend = Join-Path $solaceBase 'SOLACE_PHOTOREAL_GOAL_v01.blend'
$solaceEvidence = [IO.Path]::GetFullPath((Join-Path $solaceBase '../../evidence/solace-photoreal-goal-v01'))
foreach ($frame in 1..420) {
    $framePath = Join-Path $solaceFrames ('{0:D4}.png' -f $frame)
    if (!(Test-Path -LiteralPath $framePath)) { throw "Missing frame $frame" }
    $stream = [IO.File]::OpenRead($framePath)
    try {
        $header = New-Object byte[] 24
        if ($stream.Read($header,0,24) -ne 24) { throw "Truncated frame $frame" }
        if ([BitConverter]::ToString($header[0..7]) -ne '89-50-4E-47-0D-0A-1A-0A') { throw "Invalid PNG $frame" }
        if ([BitConverter]::ToString($header[16..23]) -ne '00-00-07-80-00-00-04-38') { throw "Not 1920x1080: $frame" }
    } finally { $stream.Dispose() }
}
if (Test-Path -LiteralPath $solaceMovie) { throw 'Movie already exists; preserve it, do not overwrite.' }
& ffmpeg -hide_banner -loglevel warning -n -framerate 30 -start_number 1 -i (Join-Path $solaceFrames '%04d.png') -frames:v 420 -c:v libx264 -preset slow -crf 18 -pix_fmt yuv420p -movflags +faststart -an $solaceMovie
if ($LASTEXITCODE -ne 0) { throw 'H264 encoding failed' }
$probeRaw = & ffprobe -v error -count_frames -show_streams -show_format -of json $solaceMovie
if ($LASTEXITCODE -ne 0) { throw 'ffprobe failed' }
$probe = ($probeRaw -join "`n") | ConvertFrom-Json
$video = $probe.streams | Where-Object codec_type -eq 'video'
if ($video.width -ne 1920 -or $video.height -ne 1080 -or $video.r_frame_rate -ne '30/1' -or $video.nb_read_frames -ne '420' -or $video.codec_name -ne 'h264') { throw 'Delivery metadata mismatch' }
if ([Math]::Abs([double]::Parse($probe.format.duration,[Globalization.CultureInfo]::InvariantCulture)-14) -gt .001) { throw 'Duration mismatch' }
& ffmpeg -v error -xerror -i $solaceMovie -f null -
if ($LASTEXITCODE -ne 0) { throw 'Full video decode failed' }
$blackLog = & ffmpeg -hide_banner -i $solaceMovie -vf 'blackdetect=d=0.033:pix_th=0.02:pic_th=0.98' -an -f null - 2>&1
if ($LASTEXITCODE -ne 0) { throw 'Black-frame analysis failed' }
if (($blackLog -join "`n") -match 'black_start:') { throw 'Near-black frames found; inspect before delivery' }
foreach ($frame in @(1,61,121,181,241,301,361,415,420)) {
    $from = Join-Path $solaceFrames ('{0:D4}.png' -f $frame)
    $finalEvidence = Join-Path $solaceEvidence 'final-render'
    [IO.Directory]::CreateDirectory($finalEvidence) | Out-Null
    $to = Join-Path $finalEvidence ('anchor_{0:D4}.png' -f $frame)
    if (Test-Path -LiteralPath $to) { throw "Evidence exists: $to" }
    Copy-Item -LiteralPath $from -Destination $to
}
$result = [ordered]@{
    status='TECHNICALLY_VALID_REVIEW_CANDIDATE';human_visual_review='PENDING'
    frames=420;duration_seconds=14;fps=30;resolution=@(1920,1080);codec='H264';audio=$false
    full_decode='PASS';black_frame_check='PASS';renderer='Cycles OPTIX';blender='5.2.1 LTS'
    blend_bytes=(Get-Item -LiteralPath $solaceBlend).Length
    blend_sha256=(Get-FileHash -LiteralPath $solaceBlend -Algorithm SHA256).Hash
    mp4_bytes=(Get-Item -LiteralPath $solaceMovie).Length
    mp4_sha256=(Get-FileHash -LiteralPath $solaceMovie -Algorithm SHA256).Hash
    source='references/solace/video/VIDEO_REFERENCIA_SOLACE_CINEMATIC_TARGET.mp4'
    scene_stage='assembly_r12';visual_approval='NOT_CLAIMED'
}
[IO.File]::WriteAllText((Join-Path $solaceEvidence 'technical-verification.json'),($result | ConvertTo-Json -Depth 5))
$result | ConvertTo-Json -Depth 5
