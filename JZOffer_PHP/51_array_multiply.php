<?php
运行时间：60ms

占用内存：2424k
	function multiply($numbers)
	{
		if (empty($numbers) || count($numbers) <= 0) {
			return [];
		}
		$length = count($numbers);
		$mulNums = array();
		$mulNums[0] = 1;
		for ($i = 1; $i < $length; $i++) {
			$mulNums[$i] = $mulNums[$i - 1] * $numbers[$i]; 
		}
		
		$temp = 1;
		for ($i = $length - 2; $i >= 0; $i--) {
			$temp *= $numbers[$i + 1];
			$mulNums[$i] *= $temp 
		}
		return $mulNums;
	}
?>