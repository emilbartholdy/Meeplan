
using System;
using System.Collections.Generic;
using System.Linq;

public class ParseScheduleRequirements {
    public static int ParseNumberOfEmployees(string employeeNumberString)
    {
        var employeeNumber = 0;
        int.TryParse(employeeNumberString, out employeeNumber);
        
        return employeeNumber;
    }

    public static int ParseWeekNumber(string weekString)
    {
        var weekNumber = 0;
        int.TryParse(weekString, out weekNumber);
        
        return weekNumber;
    }

    public static (int, int, int)[] ParseFixedAssignments(string[] fixedAssignmentsStrings)
    {
        return fixedAssignmentsStrings
                    .Select(l => l.Split(" ").Select(c => int.Parse(c)).ToList())
                    .ToList()
                    .Select(l => Tuple.Create(l[0], l[1], l[2]).ToValueTuple())
                    .ToList()
                    .ToArray();
    }
    
    public static (int, int, int, int)[] ParseRequests(string[] requestStrings)
    {
       return requestStrings
                    .Select(l => l.Split(" ").Select(c => int.Parse(c)).ToList())
                    .ToList()
                    .Select(l => Tuple.Create(l[0], l[1], l[2], l[3]).ToValueTuple())
                    .ToList()
                    .ToArray();
    }

    public static int[][] ParseCoverDemands(string[] coverDemandsStrings)
    {
        return coverDemandsStrings
                    .Select(l => l.Split(" ").Select(c => int.Parse(c)).ToList().ToArray())
                    .ToList()
                    .ToArray();
                    
    }

    public static ((string numEmp, string numWeeks) numbers, string[] fixedAssignments, string[] requests, string[] coverDemands) splitScheduleDescriptionIntoMainParts(string scheduleDesc) {
        var mainParts = scheduleDesc.Split("---");
        
        var numbers = mainParts[0].Split("\n").Where(c => c != "").ToArray();
        var fixedAssignments = mainParts[1].Split("\n").Where(c => c != "").ToArray();
        var requests = mainParts[2].Split("\n").Where(c => c != "").ToArray();
        var coverDemands = mainParts[3].Split("\n").Where(c => c != "").ToArray();

        return ((numbers[0], numbers[1]), fixedAssignments, requests, coverDemands);
    }
}