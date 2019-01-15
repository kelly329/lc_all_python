<?php
	/*class ListNode{
		var $val;
		var $next = NULL;
		function __construct($x){
			$this->val = $x;
		}
	}*/
	// 运行时间：295ms 占用内存：2424k
	function FindKthToTailII($head, $k)
	{
		if($head==NULL || $k == 0){
			return NULL;
		}
		
		$firstHead = $head;
		$secondHead = $head;
		
		for ($i = 0; $i < $k - 1; $i++) {
			if ($secondHead->next == NULL){
				return NULL;
			}else{
				$secondHead = $secondHead->next;
			}
		}
		
		while($secondHead->next != NULL){
			$firstHead = $firstHead->next;
			$secondHead = $secondHead->next;
		}
		return $firstHead;
	}
	// 运行时间：104ms 占用内存：2424k
	function FindKthToTailII($head, $k)
	{
		$phead = $head;
		$len = 0;
		while($head != NULL){
			$head = $head->next;
			$len++;
		}
		if($k > $len){
			return NULL;
		}
		for($i = 0; $i < ($len - $k); $i++){
			$phead = $phead->next;
		}
		return $phead;
		
		
	}
?>