<?php

require_once "database.php";

class Functions extends Database
{

    public function compareDate($year, $month, $date)
    {
        $today = intval($year . $month . $date);
        $date = $date + 7;
        if ($date >= 29) {
            list($month, $date) = $this->adjastDate($year, $month, $date);
        }
        $date_str = $this->adjastZero($year, $month, $date);
        $date_int = intval($date_str); //string to int

        $sql = "SELECT `date`,`name`,grade,`location`,age,style,distance FROM race_list WHERE `date` <= $date_int && `date` >= $today";
        $result = $this->conn->query($sql);

        $race_name_list = new ArrayObject();

        while ($race_name = $result->fetch_assoc()) {
            $race_name_list->append($race_name);
        }
        return $race_name_list;
    }

    public function adjastZero($year, $month, $date)
    {
        if (strlen($month) == 1) {
            $month = "0" . $month;
        }
        if (strlen($date) == 1) {
            $date = "0" . $date;
        }

        $date_str = $year . $month . $date;
        return $date_str;
    }

    public function adjastDate($year, $month, $date)
    {
        switch ($month) {
            case 1:
            case 3:
            case 5:
            case 7:
            case 8:
            case 10:
            case 12:
                if ($date >= 32) {
                    $date = $date % 31;
                    $month += 1;
                }
                break;
            case 2:
                if ($year % 4 == 0) {
                    $date = $date % 29;
                    $date += 1;
                    $month += 1;
                } else {
                    $date = $date % 28;
                    $month += 1;
                }
                break;
            case 4:
            case 6:
            case 9:
            case 11:
                if ($date >= 31) {
                    $date = $date % 30;
                    $month += 1;
                }
                break;
        }
        return [$month, $date];
    }
}
