<?php
//	运行时间：26ms
//
//	占用内存：2776k
	function jumpFloorII($number)
	{
		// write code here
		if ($number <= 0){
			return -1;
		} elseif ($number == 1) {
			return 1;
		} else {
			return 2 * jumpFloorII($number - 1);
		}
	}
	// 根据等比数列性质：an = a1 * q^(n-1) 此题 an = 2^(n - 1)
	function jumpFloorI($number)
	{
		if($number == 0){
			return 0;
		} 
		$total = 1;
		for($i = 1; $i < $number; $i++){
			$total *= 2;
		}
		return $total;
		
	}
?>