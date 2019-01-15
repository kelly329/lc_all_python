<?php
	运行时间：68ms

	占用内存：7780k
	/*class ListNode{
		var $val;
		var $next = NULL;
		function __construct($x){
			$this->val = $x;
		}
	}*/
	function printListFromTailToHead($head)
	{
		// write code here
		$list = [];
		$curNode = $head;
		while($curNode != NULL){
			$list[] = $curNode->val;
			$curNode = $curNode->next;
		}
		return array_reverse($list);
	}
?>