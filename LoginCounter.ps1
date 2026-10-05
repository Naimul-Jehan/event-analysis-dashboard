$ExportPath = "D:\Career_Development\Python\Project\Gemini_Project\Event_Analysis\daily_login_counts.csv"
$Yesterday = (Get-Date).Date.AddDays(-1)
$Today = (Get-Date).Date

# Query only yesterday's events
$events = Get-WinEvent -FilterHashtable @{LogName='Security'; Id=4624; StartTime=$Yesterday; EndTime=$Today} -ErrorAction SilentlyContinue

$count = 0
if ($events) { $count = $events.Count }

# Create a summary row and append it to the CSV
[PSCustomObject]@{
    Date = $Yesterday.ToString('yyyy-MM-dd')
    Count = $count
} | Export-Csv $ExportPath -NoTypeInformation -Append