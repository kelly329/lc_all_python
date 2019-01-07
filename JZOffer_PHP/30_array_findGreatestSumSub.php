<?php
	function FindGreatestSumOfSubArray($array)
	{
		if (empty($array) || count($array) <= 0) {
			return 0;
		}
		
		$curSum = $array[0];
		$maxSum = $array[0];
		for($i = 1; $i < count($array); $i++){
			if($curSum <= 0){
				$curSum = $array[$i];
			}else{
				$curSum += $array[$i];
			}
			if($curSum > $maxSum){
				$maxSum = $curSum;
			}
		}
		return $maxSum;
	}
?>