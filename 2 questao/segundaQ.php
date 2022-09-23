<?php
    $valor_num = $_POST["numero"];
    $result = $valor_num % 2;
    if($result == 0){
        echo $valor_num." é par";
        if($valor_num > 0){
            echo " e positivo";
        }
        elseif($valor_num <0){
            echo " e negativo";
        }
    }
    elseif($result != 0){
        echo $valor_num." é ímpar";
        if($valor_num > 0){
            echo " e positivo";
        }
        elseif($valor_num <0){
            echo " e negativo";
        }
    }

?>