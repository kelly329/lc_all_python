<?php
    运行时间：30ms

    占用内存：2504k
	function duplicate($numbers, &$duplication)
	{
		
		//这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
		//函数返回True/False
		$length = count($numbers);
		if (empty($numbers) || $length <= 0):
			return false;
		
		foreach ($numbers as $item) {
			if ($item < 0 || $item > $length - 1) {
				return false;
			}
		}
		
		for ($i = 0; $i < $length; $i++ ) {
			while ($i != $numbers[$i]) {
				
				if($numbers[$i] == $numbers[$numbers[$i]]){
					$duplication[0] = $numbers[$i];
					return true;
				}
				
				$temp = $numbers[$i];
				$numbers[$i] = $numbers[$temp];
				$numbers[$temp] = $temp;
			}
		}
		
	}
?>