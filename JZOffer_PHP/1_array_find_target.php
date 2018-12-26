<?php
	
function Find($target, $array)
{
	//var_dump($array);
	var_dump(count($array));
	var_dump(count($array[0]));
	foreach ($array as $item) {
		foreach ($item as $value) {
			
			if ($value == $target){
				
				return  True;
			}
		}
	}
		return false;
		//$rows = count($array);
		//$cols = count($array[0]);
}

function FindTarget($target, $array)
{
	$rows = count($array);
	$cols = count($array[0]);
	if(!empty($array) && $rows > 0 && $cols > 0){
		$row = 0;
		$col = $cols - 1;
	

		while ($row < $rows && $col >= 0) {
			if($array[$row][$col] > $target){
				$col -= 1;
			}elseif ($array[$row][$col] < $target){
				$row += 1;
			}else{
				return True;
			}
		}
	}
	
	
	if(!empty($array) && $rows > 0 && $cols > 0){
		$row = $rows - 1;
		$col = 0;
	

		while ($row >= 0 && $col < $cols) {
			if($array[$row][$col] > $target){
				$row -= 1;
			}elseif ($array[$row][$col] < $target){
				$col += 1;
			}else{
				return True;
			}
		}
	}
	
	return false;
	
}
//$array = [[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]];
//$array = array(array(1,2,8,9),array(2,4,9,12),array(4,7,10,13),array(6,8,11,15),array(9,10,12,17));
$array = array();
$target = 18;
var_dump Find($target, $array);

//function  Result($arr){
//	if($arr == True){
//		echo "找到！\n";
//	}else{
//		echo "没有找到！\n";
//	}
//	
//}
//Result(Find($target, $array));
//Result(FindTarget($target, $array));
?>