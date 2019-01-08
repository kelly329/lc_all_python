<?php
    // 不添加约束条件（奇数与奇数/偶数与偶数相对位置不变）
//	function reOrderArray($array)
//	{
//		if ($array == null || count($array) <= 0) {
//			return;
//		}
//		$pBegin = 0;
//		$pEnd = count($array) - 1;
//		while ($pBegin < $pEnd) {
//			while ($pBegin < $pEnd && ($array[$pBegin] & 0x1) != 0) {
//				$pBegin++;
//			}
//			
//			while ($pBegin < $pEnd && ($array[$pEnd] & 0x1)== 0) {
//				$pEnd--;
//			}
//			
//			if($pBegin < $pEnd){
//				$temp = $array[$pBegin];
//				$array[$pBegin] = $array[$pEnd];
//				$array[$pEnd] = $temp;
//			}
//		}
//		return $array;
//	}
	$array = array(3,5,8,9,10,20,23,4,7,11);
//	print_r(reOrderArray($array));
	
	//考虑约束条件（双向队列）
	function reOrderArrayQue($array) {
		if ($array == null || count($array) <= 0) {
			return;
		}
		$result = array();
		
		$num = count($array);
		for ($i = 0; $i < $num; $i++) {
			if ($array[$num - $i - 1] % 2 != 0) {
				array_unshift($result, $array[$num - $i - 1]);
			}
			if ($array[$i] % 2 == 0) {
				array_push($result, $array[$i]);
			}
		}
		return $result;
	}
	print_r(reOrderArrayQue($array));
?>