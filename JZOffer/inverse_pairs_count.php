<?php
    
	function InversePairs($data)
	{
		if (count($data) < 0 || empty($data)){
			return 0;
		}
		// var_dump($data);
		$lengths = count($data);
		// $curArr = $data;
		$curArr = array();
		foreach ($data as $key => $val) {
			$curArr[$key] = $val;
		}
		return InversePairsCount($data,$curArr,0,$lengths - 1);
	}
	
	function InversePairsCount($data, $curArr, $start, $end){
		if($start == $end){
			$curArr[$start] = $data[$start];
			return 0;
		}
		
		$length = ($end - $start) / 2;
		$left = InversePairsCount($curArr, $data, $start, $start + $length);
		$right = InversePairsCount($curArr, $data, $start + $length + 1, $end);
		
		//i初始化为前半段最后一个数字的下标
		$i = $start + $length;
		//j初始化为后半段最后一个数字的下标
		$j = $end;
		$indexCur = $end;
		$count = 0;
		
		while ($i >= $start && $j >= $start + $length + 1) {
			if($data[$i] > $data[$j]){
				$curArr[$indexCur--] = $data[$i--];
				$count += $j - $start - $length;
			} else {
				$curArr[$indexCur--] = $data[$j--];
			}
		}
		
		for(;$i >= $start; --$i){
			$curArr[$indexCur--] = $data[$i];
		}
		for(;$j >= $start + $length + 1; --$j){
			$curArr[$indexCur--] = $data[$j];
		}
		$sum = $left + $right + $count;
		return $sum;
	}
	$data = array('1','2','3','4','5','6','7','0');
	InversePairs($data);
?>