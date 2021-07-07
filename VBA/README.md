# My VBA Practice
VBA, maybe it could my ancient future
- Sigma3 (2021.07.07)
- Sigma2 (2021.01.03)
- Sigma (2021.01.02)
- Color_Scroll (2020.11.14)


## Sigma3 (2021.07.07)
- Add `Error Handler` 
- How about naming labels such like `try` ~ `catch` ~ `finally`?

![Sigma3](Images/VBA_Sigma3.PNG)

```vba
Option Explicit


Function Sigma3(k As Integer, n As Integer) As Integer

    On Error GoTo ErrorHandler

    If k > n Then
        Err.Raise 380   'Error Code 380 : Invalid property value.
    End If

    Dim i As Integer, Sum As Integer

    For i = k To n      'including both of k and n
        Sum = Sum + i
    Next i

    Sigma3 = Sum
    
    Exit Function
    

ErrorHandler:
    
    MsgBox "Error occurs : Starting number k is greater than final number n."
    
End Function
```


## Sigma2 (2021.01.03)
- Add a parameter of _k_ that indicates a starting point
- Need to add codes for handling errors.

![Sigma2](Images/VBA_Sigma2.PNG)

```vba
Option Explicit


Function Sigma2(k As Integer, n As Integer) As Integer

    Dim i As Integer, Sum As Integer

    For i = k To n
        Sum = Sum + i
    Next i

    Sigma2 = Sum

End Function
```


## Sigma (2021.01.02)
- Make a function to calculate `summation` (a.k.a. Sigma, Σ)
- Define all the variables as `integer`

![Sigma](Images/VBA_Sigma.PNG)

```vba
Option Explicit


Function Sigma(n As Integer) As Integer

    Dim i As Integer, Sum As Integer

    For i = 1 To n
        Sum = Sum + i
    Next i

    Sigma = Sum

End Function
```


## Color_Scroll (2020.11.14)
- Make a color matrix by `Nested For` statement
- Want to make it flow, but it doesn't work well yet

![Color_Scroll](Images/VBA_Color_Scroll.png)

```vba
Option Explicit

Sub Color_Scroll()

    Dim StartRow As Integer, StartColumn As Integer, Width As Integer, Height As Integer
    Dim i As Integer, j As Integer, k As Integer
    Dim FirstColumn As Range, LastColumn As Range
    
    StartRow = 1
    StartColumn = 1
    Width = 56
    Height = 56
        
    Range(Cells(StartRow, StartColumn), Cells(Height, Width)).Select
    Selection.RowHeight = 10
    Selection.ColumnWidth = 1
    
    For i = 1 To Height
        For j = 1 To Width
            Cells(i, j).Interior.ColorIndex = (i + j) Mod 56 + 1
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
