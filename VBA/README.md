# My VBA Practice
VBA, it may be my ancient futures
- Color_Scroll (2020.11.14)

## Color_Scroll (2020.11.14)
- Make color matrix by `Nested For` statement
- Want to make it flow, but it doesn't work well yet

![Color_Scroll](https://github.com/kimpro82/MyPractice/blob/master/images/VBA_Color_Scroll.png)

```vba
Option Explicit

Sub Color_Scroll()

    Dim StartRow As Integer, StartColumn As Integer, Width As Integer, Height As Integer
    Dim i As Integer, j As Integer, k As Integer
    Dim FirstColumn As Range, LastColumn As Range
    
    StartRow = 1
    StartColumn = 1
    Width = 112
    Height = 50
        
    Range(Cells(StartRow, StartColumn), Cells(Height, Width)).Select
    Selection.RowHeight = 10
    Selection.ColumnWidth = 1
    
    For i = 1 To Height
        For j = 1 To Width
            Cells(i, j).Interior.ColorIndex = (i + j) Mod 56 + 1 '
        Next j
    Next i
    
'Differnt result from debugging mode and normal run mode(F5)
'    For k = 1 To Width
'        Columns(Width).Select
'        Selection.Cut
'        Columns(1).Select
'        Selection.Insert Shift:=xlToRight
'    Next k
    
End Sub
```

```vba
Sub Reset()
'Initialize the sheet

    Cells.Select
    Selection.Clear
    
    Selection.ColumnWidth = 10
    Selection.RowHeight = 15

End Sub
```
