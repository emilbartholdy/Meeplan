# Dependencies
* Python 3.7
* Pandas

# Publish
Publish C# part (macOS):

`dotnet publish -r osx-x64 -c release /p:publishsinglefile=true`

Very similar for windows/linux.

## Running published C# part
`./PlannerCSharp /schedule-description.txt`
