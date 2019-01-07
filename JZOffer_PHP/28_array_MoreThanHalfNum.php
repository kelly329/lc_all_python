<?php
    $r_inputInvaild = false;

	function MoreThanHalfNum_Solution($numbers)
	{
		
		if(CheckInvalidArray($numbers)){
			return 0;
		}
		
		$result = $numbers[0];
		$times = 1;
		for($i = 1; $i < count($numbers); $i++){
			if ($times == 0) {
				$result = $numbers[$i];
				$times = 1;
			} elseif ($result == $numbers[$i]){
				$times++;
			} else {
				$times--;
			}
		}
		// 使用foreach也是可以的
//		foreach ($numbers as $key => $value) {
//			if($key == 0){
//				continue;
//			}
//			if ($times == 0) {
//				$result = $value;
//				$times = 1;
//			} elseif ($result == $value){
//				$times++;
//			} else {
//				$times--;
//			}
//		}
		if(!CheckMoreThanHalf($numbers,$result)){
			$result = 0;
		}

		return $result;
	}
	function CheckInvalidArray($numbers){
		$r_inputInvaild = false;
		if (empty($numbers) || count($numbers) <= 0) {
			$r_inputInvaild = true;
		}
		return $r_inputInvaild;
	}
	//输入数组中出现频率高的数组没有达到超过数组长度一半的标准
	function CheckMoreThanHalf($numbers,$result){
		$times = 0;
		foreach ($numbers as $item) {
			if($item == $result){
				$times++;
			}
		}
		$isMoreThanHalf = true;
		if($times * 2 <= count($numbers)){
			$isMoreThanHalf = false;
			$r_inputInvaild = true;
		}
		return $isMoreThanHalf;
	}
	var_dump(MoreThanHalfNum_Solution(array(1,2,3,2,2,2,5,4,2)));
?>