<?php
运行时间：70ms

占用内存：2752k
function PrintMinNumber($numbers)
{
	if(empty($numbers) || count($numbers) <= 0){
		return "";
	}
	usort($numbers, 'ReSorted');
	$res = "";
	for($i = 0; $i < count($numbers); $i++){
		
		$res .= $numbers[$i];
	}
	
	return $res;
	
}
function ReSorted($str1, $str2){
	$strA = $str1.$str2;
	$strB = $str2.$str1;
	// 如果第一个数大于第二个数 1 
	return ($strA < $strB)? -1 : 1 ;
}
	
var_dump(PrintMinNumber(array(3, 32, 321)));
?>

