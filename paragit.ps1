New-Item -Path 'C:\' -Name 'ejercicio' -ItemType 'directory'
Set-Location 'C:\ejercicio'
New-Item hola.txt
Copy-Item hola.txt hola.bak