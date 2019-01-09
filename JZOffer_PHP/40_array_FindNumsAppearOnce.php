<?php
运行时间：303ms

占用内存：2648k
	function FindNumsAppearOnce($array)
	{
		// write code here
		// return list, 比如[a,b]，其中ab是出现一次的两个数字
		if (empty($array) || count($array) < 2){
			return [];
		}
		
		$xor = 0;
		foreach($array as $arr){
			$xor ^= $arr;
		}
//		var_dump($xor);
		$bitLocation = FindOneLocation($xor);
//		var_dump($bitLocation);
		$num1 = 0;
		$num2 = 0;
		foreach($array as $arr){
			if(IsSameLocation($arr, $bitLocation)){
				$num1 ^= $arr;
			}else{
				$num2 ^= $arr;
			}
		}
		
		return array($num1, $num2);
		
	}
	function FindOneLocation($num){
		$bitCount = 0;
		while (($num & 1) == 0 && $bitCount <= 32){
			$bitCount++;
			$num = $num >> 1;
		}
		var_dump($bitCount);
		return $bitCount;
	}
	function IsSameLocation($num, $location){
		$num = $num >> $location;
//		if(($num & 1) == 0){
//			return false;
//		} else {
//			return true;
//		}
        return ($num & 1);
	}
	
	var_dump(FindNumsAppearOnce(array(2,4,3,6,3,2,5,5)));
?>