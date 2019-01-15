<?php
	运行时间：20ms

	占用内存：8208k
	function jumpFloor($number)
	{
		
		// write code here
		if ($number < 3){
			return $number;
		}
		$f1 = 1;
		$f2 = 2;
		for($i=3; $i <= $number; $i++){
			$temp = $f1 + $f2;
			$f1 = $f2;
			$f2 = $temp;
		}
		return $temp;
	}
?>