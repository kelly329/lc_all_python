<?php
	function minNumberInRotateArray($rotateArray)
	{
		if(count($rotateArray) == 0 || empty($rotateArray)){
			return 0;
		}
		$length = count($rotateArray);
		$left = 0;
		$right = $length - 1;
		//如果是已经旋转后的数组，所以才会有此句
		$indexMid = $left;
		while ($rotateArray[$left] >= $rotateArray[$right]) {
			
			if($right - $left == 1){
				return $rotateArray[$right];
				break;
			}
			
			$indexMid = ($left + $right) / 2;
			
			if($rotateArray[$left] == $rotateArray[$right] && $rotateArray[$indexMid] == $rotateArray[$left]){
				return findMin($rotateArray, $left, $right);
			}
			
			if($rotateArray[$indexMid] >= $rotateArray[$left]){
				$left = $indexMid;
			}elseif ($rotateArray[$indexMid] <= $rotateArray[$right]){
				$right = $indexMid;
			}
		}
	    return $rotateArray[$indexMid];
	}
	function finMin($rotateArray, $left, $right){
		$result = $rotateArray[$left];
		$index = $left + 1;
		for($index;$index <= $right; ++$index){
			if($result > $rotateArray[$index]){
				$result = $rotateArray[$index];
			}
		}
		return $result;
	}
	var_dump(minNumberInRotateArray(array(4,5,7,9,10,0,1,2,3)));
	
	
	
	
	
	function minNumberInRotateArray($rotateArray)
	{
		if($rotateArray == null){
			return 0;
		}
		$little = 0;
		$high = count($rotateArray) - 1;
		if($rotateArray[$little] < $rotateArray[$high]){    //如果旋转数组已经是按从小到大排序，那就无需查找，第一个数就是最小的
			return $rotateArray[0];
		}
		while ($little < $high){        //如果左边下标比右边下标小，则进入循环
			if($high == $little + 1){   //如果右边下标就是坐标下边的下一个值，证明最小值找到了，它就是右边下标指向的值
				return $rotateArray[$high];
			}

			$mid = floor(($little + $high)/2);
			if($rotateArray[$little] == $rotateArray[$mid] && $rotateArray[$high] == $rotateArray[$mid]){
				//如果三个索引值相等，那么无法区分中间值归属于前面还是后面，就只能顺序查找
				return midSearch($rotateArray,$little,$high);
			}
			if($rotateArray[$little] <= $rotateArray[$mid]){ //注意这里的等号！！！！！如果这里没有等号，那么对于数组[5,5,5,1,2]，就会陷入死循环
				$little = $mid;
			}
			elseif ($rotateArray[$high] >= $rotateArray[$mid]){//注意这里的等号！！！！！
				$high = $mid;
			}

		}

	}
	function midSearch($rotateArray,$index1,$index2){ //遍历查找两个索引之间的最小值
		$min = $rotateArray[$index1];
		for($i = $index1 + 1;$i<=$index2;$i++){
			if($rotateArray[$i] < $min){
				$min = $rotateArray[$i];
			}
		}
		return $min;

	}

?>