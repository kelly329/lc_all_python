<?php
	function InversePairs($data)
	{
		// write code here
		if(!$data){
			return 0;
		}
		$copy = $data;
		$count = count($data);
		return InversePairCore($data, $copy,0, $count - 1) % 1000000007 ;
	}
	function InversePairCore(&$data, &$copy, $start,$end){
		if($start == $end){
			$copy[$start] = $data[$start];
			 return 0;
		}
		$middle = (int)(($end + $start)/2);
		$left = InversePairCore($copy, $data, $start, $middle);
		$right = InversePairCore($copy, $data, $middle+1, $end);
		 
		$i = $middle;
		$j = $end;
		$indexCopy = $end;
		$count = 0;
		 
		while($i >= $start && $j >= $middle + 1){
			if($data[$i] > $data[$j]){
				 $copy[$indexCopy--] = $data[$i--];
				 $count += ($j-$middle);
			}else{
				$copy[$indexCopy--] = $data[$j--];
			}
		}
		while ($i >= $start){
			$copy[$indexCopy--] = $data[$i--];
		}
		while($j >= $middle + 1){
			$copy[$indexCopy--] = $data[$j--];
		}
		
		return $count+$left+$right;
	}
	var_dump(InversePairs(array(364,637,341,406,747,995,234,971,571,219,993,407,416,366,315,301,601,650,418,355,460,505,360,965,516,648,727,667,465,849,455,181,486,149,588,233,144,174,557,67,746,550,474,162,268,142,463,221,882,576,604,739,288,569,256,936,275,401,497,82,935,983,583,523,697,478,147,795,380,973,958,115,773,870,259,655,446,863,735,784,3,671,433,630,425,930,64,266,235,187,284,665,874,80,45,848,38,811,267,575)));
?>