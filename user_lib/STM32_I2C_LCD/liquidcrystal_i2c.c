/*
 * liquidcrystal_i2c.c
 *
 *  Created on: 2025. 03. 12.
 *      Author: Lee Yongjin
 *
 * STM32 HAL library for LCD display based on 16x2 CLCD with PCF8574
 */

#include "liquidcrystal_i2c.h"
#include "stm32f1xx_hal.h"
#include "stm32f1xx_hal_i2c.h"

extern I2C_HandleTypeDef hi2c1;


/*
 * LCD delay function
 *
 * Renamed from delay_us() to LCD_delay_us()
 * to avoid conflict with delay_us() in dht11.c.
 */
static void LCD_delay_us(int us)
{
    volatile int delay;
    int value = 3;

    delay = us * value;

    for (volatile int i = 0; i < delay; i++);
}


/*
 * Send data to LCD
 */
void LCD_DATA(int data)
{
    uint8_t temp;

    /* Upper 4 bits */
    temp = (uint8_t)((data & 0xF0) | RS1_EN1 | BackLight);

    while (HAL_I2C_Master_Transmit(
               &hi2c1,
               ADDRESS,
               &temp,
               1,
               1000) != HAL_OK);

    temp = (uint8_t)((data & 0xF0) | RS1_EN0 | BackLight);

    while (HAL_I2C_Master_Transmit(
               &hi2c1,
               ADDRESS,
               &temp,
               1,
               1000) != HAL_OK);

    LCD_delay_us(4);


    /* Lower 4 bits */
    temp = (uint8_t)(((data << 4) & 0xF0) | RS1_EN1 | BackLight);

    while (HAL_I2C_Master_Transmit(
               &hi2c1,
               ADDRESS,
               &temp,
               1,
               1000) != HAL_OK);

    temp = (uint8_t)(((data << 4) & 0xF0) | RS1_EN0 | BackLight);

    while (HAL_I2C_Master_Transmit(
               &hi2c1,
               ADDRESS,
               &temp,
               1,
               1000) != HAL_OK);

    LCD_delay_us(50);
}


/*
 * Send command to LCD
 */
void LCD_CMD(int cmd)
{
    uint8_t temp;

    /* Upper 4 bits */
    temp = (uint8_t)((cmd & 0xF0) | RS0_EN1 | BackLight);

    while (HAL_I2C_Master_Transmit(
               &hi2c1,
               ADDRESS,
               &temp,
               1,
               1000) != HAL_OK);

    temp = (uint8_t)((cmd & 0xF0) | RS0_EN0 | BackLight);

    while (HAL_I2C_Master_Transmit(
               &hi2c1,
               ADDRESS,
               &temp,
               1,
               1000) != HAL_OK);

    LCD_delay_us(4);


    /* Lower 4 bits */
    temp = (uint8_t)(((cmd << 4) & 0xF0) | RS0_EN1 | BackLight);

    while (HAL_I2C_Master_Transmit(
               &hi2c1,
               ADDRESS,
               &temp,
               1,
               1000) != HAL_OK);

    temp = (uint8_t)(((cmd << 4) & 0xF0) | RS0_EN0 | BackLight);

    while (HAL_I2C_Master_Transmit(
               &hi2c1,
               ADDRESS,
               &temp,
               1,
               1000) != HAL_OK);

    LCD_delay_us(50);
}


/*
 * Send 4-bit command to LCD
 *
 * Used during LCD initialization.
 */
void LCD_CMD_4bit(int cmd)
{
    uint8_t temp;

    temp = (uint8_t)(((cmd << 4) & 0xF0) | RS0_EN1 | BackLight);

    while (HAL_I2C_Master_Transmit(
               &hi2c1,
               ADDRESS,
               &temp,
               1,
               1000) != HAL_OK);

    temp = (uint8_t)(((cmd << 4) & 0xF0) | RS0_EN0 | BackLight);

    while (HAL_I2C_Master_Transmit(
               &hi2c1,
               ADDRESS,
               &temp,
               1,
               1000) != HAL_OK);

    LCD_delay_us(50);
}


/*
 * Initialize LCD
 */
void LCD_INIT(void)
{
    HAL_Delay(100);

    LCD_CMD_4bit(0x03);
    HAL_Delay(5);

    LCD_CMD_4bit(0x03);
    LCD_delay_us(100);

    LCD_CMD_4bit(0x03);
    LCD_delay_us(100);

    LCD_CMD_4bit(0x02);
    LCD_delay_us(100);

    LCD_CMD(0x28);      // 4-bit mode, 2 lines, 5x8 font
    LCD_CMD(0x08);      // Display off, cursor off, blink off
    LCD_CMD(0x01);      // Clear display

    HAL_Delay(3);

    LCD_CMD(0x06);      // Entry mode: cursor moves right
    LCD_CMD(0x0C);      // Display on, cursor off, blink off
}


/*
 * Set LCD cursor position
 *
 * x : column
 * y : row
 */
void LCD_XY(char x, char y)
{
    if (y == 0)
        LCD_CMD(0x80 + x);
    else if (y == 1)
        LCD_CMD(0xC0 + x);
    else if (y == 2)
        LCD_CMD(0x94 + x);
    else if (y == 3)
        LCD_CMD(0xD4 + x);
}


/*
 * Clear LCD
 */
void LCD_CLEAR(void)
{
    LCD_CMD(0x01);
    HAL_Delay(2);
}


/*
 * Display string
 */
void LCD_PUTS(char *str)
{
    while (*str)
    {
        LCD_DATA(*str++);
    }
}
