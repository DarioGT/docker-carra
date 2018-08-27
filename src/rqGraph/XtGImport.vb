# Sub XtGImport()
# '
# ' XtGImport Macro
# '
# ' Keyboard Shortcut: Ctrl+i
# '
# Dim mySheet As String
# Dim myFormula As String

# For Each Query In ActiveWorkbook.Queries
#     ActiveWorkbook.Queries.Item(Query.Name).Delete
# Next

# For Each Connection In ActiveWorkbook.Connections
#     If Not Connection.Name = "ThisWorkbookDataModel" Then
#     Connection.Delete
#     'ActiveWorkbook.Connections.Item(Connection.Name).Delete
#     End If
# Next


# Application.FileDialog(msoFileDialogOpen).AllowMultiSelect = False
# If Application.FileDialog(msoFileDialogOpen).Show = 0 Then Exit Sub
    
# myFile = Application.FileDialog(msoFileDialogOpen).SelectedItems(1)

# mySheet = "GVGraph_Attributes"
# GVGraphAttributes.Select
# Application.ActiveSheet.Range("A1").Select
# myFormula = "let" & Chr(13) & "" & Chr(10) & "    Source = Excel.Workbook(File.Contents(""" + myFile + """), null, true)," & Chr(13) & "" & Chr(10) _
#           & "    " & mySheet & "_Table = Source{[Item=""" & mySheet & """,Kind=""Table""]}[Data]" & Chr(13) & "" & Chr(10) _
#           & "in" & Chr(13) & "" & Chr(10) _
#           & "    " & mySheet & "_Table"

# emptySheetAndTable rangeName:=mySheet
# InsertTableToSheet sheetName:=mySheet, theFormula:=myFormula, theTableStyle:="TableStyleMedium9"

# mySheet = "Enum_Cluster_Type"
# Enum_GVCluster_type.Select
# Application.ActiveSheet.Range("A1").Select
# myFormula = "let" & Chr(13) & "" & Chr(10) & "    Source = Excel.Workbook(File.Contents(""" + myFile + """), null, true)," & Chr(13) & "" & Chr(10) _
#           & "    " & mySheet & "_Table = Source{[Item=""" & mySheet & """,Kind=""Table""]}[Data]" & Chr(13) & "" & Chr(10) _
#           & "in" & Chr(13) & "" & Chr(10) _
#           & "    " & mySheet & "_Table"
# emptySheetAndTable rangeName:=mySheet
# InsertTableToSheet sheetName:=mySheet, theFormula:=myFormula, theTableStyle:="TableStyleMedium14"

# mySheet = "Enum_Edge_type"
# Enum_GVEdge_type.Select
# Application.ActiveSheet.Range("A1").Select
# myFormula = "let" & Chr(13) & "" & Chr(10) & "    Source = Excel.Workbook(File.Contents(""" + myFile + """), null, true)," & Chr(13) & "" & Chr(10) _
#           & "    " & mySheet & "_Table = Source{[Item=""" & mySheet & """,Kind=""Table""]}[Data]" & Chr(13) & "" & Chr(10) _
#           & "in" & Chr(13) & "" & Chr(10) _
#           & "    " & mySheet & "_Table"
# emptySheetAndTable rangeName:=mySheet
# InsertTableToSheet sheetName:=mySheet, theFormula:=myFormula, theTableStyle:="TableStyleMedium14"
    
# mySheet = "Enum_Node_type"
# Enum_GVNode_type.Select
# Application.ActiveSheet.Range("A1").Select
# myFormula = "let" & Chr(13) & "" & Chr(10) & "    Source = Excel.Workbook(File.Contents(""" + myFile + """), null, true)," & Chr(13) & "" & Chr(10) _
#           & "    " & mySheet & "_Table = Source{[Item=""" & mySheet & """,Kind=""Table""]}[Data]" & Chr(13) & "" & Chr(10) _
#           & "in" & Chr(13) & "" & Chr(10) _
#           & "    " & mySheet & "_Table"
    
# emptySheetAndTable rangeName:=mySheet
# InsertTableToSheet sheetName:=mySheet, theFormula:=myFormula, theTableStyle:="TableStyleMedium14"

# mySheet = "Clusters"
# GVClusters.Select
# Application.ActiveSheet.Range("A1").Select
# myFormula = "let" & Chr(13) & "" & Chr(10) & "    Source = Excel.Workbook(File.Contents(""" + myFile + """), null, true)," & Chr(13) & "" & Chr(10) _
#           & "    " & mySheet & "_Table = Source{[Item=""" & mySheet & """,Kind=""Table""]}[Data]" & Chr(13) & "" & Chr(10) _
#           & "in" & Chr(13) & "" & Chr(10) _
#           & "    " & mySheet & "_Table"
# emptySheetAndTable rangeName:=mySheet
# InsertTableToSheet sheetName:=mySheet, theFormula:=myFormula, theTableStyle:="TableStyleMedium11"

# mySheet = "Cluster_Structure"
# GVCluster_Structure.Select
# Application.ActiveSheet.Range("A1").Select
# myFormula = "let" & Chr(13) & "" & Chr(10) & "    Source = Excel.Workbook(File.Contents(""" + myFile + """), null, true)," & Chr(13) & "" & Chr(10) _
#           & "    " & mySheet & "_Table = Source{[Item=""" & mySheet & """,Kind=""Table""]}[Data]" & Chr(13) & "" & Chr(10) _
#           & "in" & Chr(13) & "" & Chr(10) _
#           & "    " & mySheet & "_Table"
# emptySheetAndTable rangeName:=mySheet
# InsertTableToSheet sheetName:=mySheet, theFormula:=myFormula, theTableStyle:="TableStyleMedium11"

# mySheet = "Edges"
# GVEdges.Select
# Application.ActiveSheet.Range("A1").Select
# myFormula = "let" & Chr(13) & "" & Chr(10) & "    Source = Excel.Workbook(File.Contents(""" + myFile + """), null, true)," & Chr(13) & "" & Chr(10) _
#           & "    " & mySheet & "_Table = Source{[Item=""" & mySheet & """,Kind=""Table""]}[Data]" & Chr(13) & "" & Chr(10) _
#           & "in" & Chr(13) & "" & Chr(10) _
#           & "    " & mySheet & "_Table"
# emptySheetAndTable rangeName:=mySheet
# InsertTableToSheet sheetName:=mySheet, theFormula:=myFormula, theTableStyle:="TableStyleMedium11"
    
# mySheet = "Nodes"
# GVNodes.Select
# Application.ActiveSheet.Range("A1").Select
# myFormula = "let" & Chr(13) & "" & Chr(10) & "    Source = Excel.Workbook(File.Contents(""" + myFile + """), null, true)," & Chr(13) & "" & Chr(10) _
#           & "    " & mySheet & "_Table = Source{[Item=""" & mySheet & """,Kind=""Table""]}[Data]" & Chr(13) & "" & Chr(10) _
#           & "in" & Chr(13) & "" & Chr(10) _
#           & "    " & mySheet & "_Table"
    
# emptySheetAndTable rangeName:=mySheet
# InsertTableToSheet sheetName:=mySheet, theFormula:=myFormula, theTableStyle:="TableStyleMedium11"
        
# End Sub
# Function InsertTableToSheet(sheetName As String, theFormula As String, theTableStyle As String)

#     ActiveWorkbook.Queries.Add Name:=sheetName, Formula:=theFormula
#     With ActiveSheet.ListObjects.Add(SourceType:=0, Source:= _
#         "OLEDB;Provider=Microsoft.Mashup.OleDb.1;Data Source=$Workbook$;Location=" + sheetName _
#         , Destination:=Range("$A$1")).QueryTable
#         .CommandType = xlCmdSql
#         .CommandText = Array("SELECT * FROM [" + sheetName + "]")
#         .RowNumbers = False
#         .FillAdjacentFormulas = False
#         .PreserveFormatting = True
#         .RefreshOnFileOpen = False
#         .BackgroundQuery = True
#         .RefreshStyle = xlInsertDeleteCells
#         .SavePassword = False
#         .SaveData = True
#         .AdjustColumnWidth = True
#         .RefreshPeriod = 0
#         .PreserveColumnInfo = True
#         .ListObject.DisplayName = sheetName
#         .Refresh BackgroundQuery:=False
#     End With
#     Selection.ListObject.QueryTable.Refresh BackgroundQuery:=False
#     Selection.ListObject.QueryTable.MaintainConnection = False
#     Selection.ListObject.QueryTable.Delete
#     ActiveSheet.ListObjects(sheetName).TableStyle = theTableStyle
#     ActiveWorkbook.Queries.Item(sheetName).Delete
# End Function
# Function emptySheetAndTable(rangeName As String)
#     Dim l_rangeName As String
#     l_rangeName = rangeName & "[#All]"
#     Range(l_rangeName).Select
#     Selection.ClearContents
#     Selection.Borders(xlDiagonalDown).LineStyle = xlNone
#     Selection.Borders(xlDiagonalUp).LineStyle = xlNone
#     Selection.Borders(xlEdgeLeft).LineStyle = xlNone
#     Selection.Borders(xlEdgeTop).LineStyle = xlNone
#     Selection.Borders(xlEdgeBottom).LineStyle = xlNone
#     Selection.Borders(xlEdgeRight).LineStyle = xlNone
#     Selection.Borders(xlInsideVertical).LineStyle = xlNone
#     Selection.Borders(xlInsideHorizontal).LineStyle = xlNone
#     With Selection.Interior
#         .Pattern = xlNone
#         .TintAndShade = 0
#         .PatternTintAndShade = 0
#     End With
# End Function


