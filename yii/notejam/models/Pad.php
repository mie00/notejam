<?php
namespace app\models;

use Yii;

/**
 * User model
 *
 * @property integer $id
 * @property integer $user_id
 * @property string $name
 */
class Pad extends \yii\db\ActiveRecord
{

    /**
     * @inheritdoc
     */
    public function rules()
    {
        return [
            ['name', 'required'],
        ];
    }

    /**
     * @return string the name of the table associated with
     *         this ActiveRecord class.
     */
    public static function tableName()
    {
        return 'pads';
    }
}
