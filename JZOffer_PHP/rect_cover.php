<?php
    // 运行时间：28ms 占用内存：3664k
	function rectCover($number)
	{
		if ($number <= 0){
			return 0;
		}
		if ($number == 1 || $number == 2){
			return $number;
		}
		$f1 = 1;
		$f2 = 2;
		while($number > 2){
			$temp = $f1 + $f2;
			$f1 = $f2;
			$f2 = $temp;
			$number--;
		}
		return $temp;
	}
	
	// 递归
	function rectCover($number)
	{
		if ($number <= 0){
			return 0;
		}
		if ($number == 1 || $number == 2){
			return $number;
		}
		return rectCover($number - 1) + rectCover($number - 2);
	}
	
	
?>