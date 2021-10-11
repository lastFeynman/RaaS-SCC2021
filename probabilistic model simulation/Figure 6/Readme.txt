Meanings of every subfolder:
	1) adjust_r_1: driver profile ξ = 1
	2) adjust_r_2: driver profile ξ = 2
	3) adjust_r_3: driver profile ξ = 0.5
	4) adjust_r_4: driver profile ξ = 0.1
	5) adjust_r_5: driver profile ξ = 0.7
	6) fixed: driver with fixed obey rate
	8) honest: honest driver
	9) possibility: draw the figure

Every folder above contains two subfolder:
	1) re: changing reward with fixed punishment
	2) pu: changing punishment with fixed reward



***PLEASE FOLLOW THE PROCEDURE STRICTLY***

1. Prerequisites:
	1) Python 3.x
	2) numpy
	3) matplotlib

***THE FOLLOWING PROCEDURES MAY USE UP YOUR CPU RESOURCE***

The following 2 and 3 can run concurrently

2. Run "batch_exec.py" in "honest/re/"
3. Run "batch_exec.py" in "honest/pu/"

Before proceeding, make sure that 2 and 3 have successfully finished.

The following 4-15 can run concurrently, and the order can be whatever you want.

To ensure that your computer doesn't overloaded, please run ***no more than*** 4 "batch_exec.py" at one time.

4.  Run "batch_exec.py" in "adjust_r_1/re/"
5.  Run "batch_exec.py" in "adjust_r_1/pu/"
6.  Run "batch_exec.py" in "adjust_r_2/re/"
7.  Run "batch_exec.py" in "adjust_r_2/pu/"
8.  Run "batch_exec.py" in "adjust_r_3/re/"
9.  Run "batch_exec.py" in "adjust_r_3/pu/"
10. Run "batch_exec.py" in "adjust_r_4/re/"
11. Run "batch_exec.py" in "adjust_r_4/pu/"
12. Run "batch_exec.py" in "adjust_r_5/re/"
13. Run "batch_exec.py" in "adjust_r_5/pu/"
14. Run "batch_exec.py" in "fixed/re/"
15. Run "batch_exec.py" in "fixed/pu/"

Before proceeding, make sure that 4-15 have successfully finished.

16. Run "possibility_reward.py" in "possibility/re"
17. Run "possibility_punish.py" in "possibility/pu"

Running 16 and 17 will draw Figure 6(a) and 6(b), respectively.

18. Run "possibility.py" in "possibility"

Running 18 will draw Figure 6.