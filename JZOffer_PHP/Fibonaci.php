<?php
    // 1、1、2、3、5、8、13、21、34
	function Fibo($n){
		if ($n == 0) {
			return 0;
		}
		if ($n == 1) {
			return 1;
		}
		
		return Fibo($n - 1) + Fibo($n - 2);
	}
	var_dump(Fibo(6));
	
	
	function revertString($str){
		if(!$str){
			return $str;
		}
		return revertString(substr($str,1)) . $str[0];
		
	}
	$str = 'andgkrg';
	var_dump(revertString($str));

?>