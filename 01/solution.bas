   10 REM BBC Basic was one of the first languages I had exposure to. I spent
   20 REM quite a lot of time with it in high school. Going back was a
   30 REM interesting experience but probably not one I intend to repeat.
   40
   50 REM To download an interpreter and IDE visit
   60 REM    https://www.bbcbasic.co.uk/index.html
   70
   80 REM Not really a min heap but close enough
   90 DIM MinHeap%(3)
  100 FOR I%=1 TO 3
  110   MinHeap%(I%) = 0
  120 NEXT I%
  130
  140 REM Sum groups from file tracking highest 3 totals in the min heap
  150 file = OPENIN "input.txt"
  160 Total% = 0
  170 REPEAT
  180   line$ = GET$#file
  190   IF line$ <> "" THEN
  200     Total% = Total% + VAL(line$)
  210   ELSE
  220     PROC_HeapPush(MinHeap%(), Total%)
  230     Total% = 0
  240   ENDIF
  250 ENDIF
  260 UNTIL EOF#file
  270 CLOSE#file
  280
  290 PRINT "Part 1: " MinHeap%(3)
  300 PRINT "Part 2: " SUM(MinHeap%())
  310 END
  320
  330 REM Push new item to min heap, maintaining heap invariant
  340 DEF PROC_HeapPush(MinHeap%(), Value%)
  350 IF Value% > MinHeap%(1) THEN
  360 MinHeap%(1) = Value%
  370 PROC_HeapSift(MinHeap%(), 1, 2)
  380 PROC_HeapSift(MinHeap%(), 2, 3)
  390 ENDIF
  400 ENDPROC
  410
  420 REM Helper to sift down heap and maintain invariant
  430 DEF PROC_HeapSift(MinHeap%(), Index1%, Index2%)
  440 IF MinHeap%(Index1%) > MinHeap%(Index2%) THEN
  450 Temp% = MinHeap%(Index2%)
  460 MinHeap%(Index2%) = MinHeap%(Index1%)
  470 MinHeap%(Index1%) = Temp%
  480 ENDIF
  490 ENDPROC
