## STM32Cube를 이용한 STM32 프로그래밍

### PWM Buzzer

**STM32CubeMX**와 **STM32CubeIDE**를 이용하여  **NUCLEO-F103RB**보드의 **PC7**에 **Passive Buzzer**를 연결하고 도, 레, 미, 파, 솔, 라, 시, 도 음계를 출력해보자.  

#### 개발 환경

**OS:** MS Windows11

**타겟보드:** NUCLEO-F103RB

**SW Tools:** [STM32CubeMX 6.18.1](https://www.st.com/en/development-tools/stm32cubemx.html) / [STM32CubeIDE 2.20](https://www.st.com/en/development-tools/stm32cubeide.html)

---

**CubeMX에서 설정할 Peripheral**

​	**RCC** 클럭 설정

**GPIO** PC7 TIM3 PWM출력 채널2

**TIM3**

---

새로운 STM32 프로젝트 생성을 위해 STM32CubeMX 실행 후, 타겟 설정을 위해 **ACCESS TO BOARD SELECTOR**를 클릭한다.

![](./img/stm32cubemx_select_target1.png)

New Project from Board 화면의 **PRODUCT INFO**의 **Type**에서 **Nucleo-64**를 체크한다. 

![](./img/stm32cubemx_select_target2.png)

New Project fron Board 화면의 **PRODUCT INFO**를 스크롤다운해서 **MCU/MPU Series**에서 **STM32F1**을 체크하면 화면 우측의 **Board List**가 확 줄어든 것을 볼 수 있다. 그 중에서 타겟보드로 사용중인 **NUCLEO-F103RB**를 선택 후 화면 오른쪽 상단의 **Start Project**를 클릭한다.



![](./img/stm32cubemx_start_project.png)



![](./img/stm32cubemx_init_all_periperals_with_default.png)

위 모든 주변장치들을 기본 모드로 초기화 하겠냐는 팝업창에서 	[ Yes ]를 클릭하면

**GPIO** **PA5**는 Output Push pull로,  **PC13**은 External Interrupt Mode with Rising edge trigger detection으로 설정되고

**USART2**는 **Baudrate**115200,  **Parity** none, **Data** 8bit, **Stop** 1bit가 **default**(기본값)로 설정된다.



최우선으로 설정해야 하는 것은 **RCC** 설정이다. **Pinout & Configuration**탭에서 **System Core**를 선택 후,  **RCC**를 클릭하고 바로 우측의 RCC Mode and Configuration의 Mode에서 High Speed Clock(HSE)와 Low Speed Clock(LSE)를 모두 Disable로 설정한다. 이는 모든 외부 클럭을 Disable시킨 것으로 **HSI**(High Speed Internal Clock)를 클럭 소스로 사용하겠다는 의미이다.

![](./img/stm32cubemx_rcc_config.png)

CLOCK설정 확인을 위해 **Clock Configuration**탭을 클릭하여 최초 **HSI**(High Speed Internal Clock) 8MHz를 소스 클럭으로 시작하여 64MHz의 시스템 클럭으로 공급되는 것을 확인한다.

![](./img/stm32cubemx_check_clock.png)

Buzzer가 연결된 PC7을 TIM3의 PWM출력 채널 2번으로 설정.

![](./img/stm32cubemx_config_tim3_n_pc7.png)

TIM3의 Mode and Configuration에서

Clock Source를 Internal Clock으로, Channel2를 PWM Generation CH2로, Prescaler를 64-1로 설정한다.

여기까지 설정을 반영한 코드 생성을위해 **Generate Code**를 클릭 하기 전 **STM32CubeMX**에서 생성한 프로젝트들을 저장해 둘 폴더를 만들어 두어야 한다. 그 위치는 편의상 **STM32CubeIDEworkspace_2.2.0** 폴더와 같은 폴더에, 폴더 이름은 **STM32CubeProjects**(폴더 이름은 다른 임의의이름(영문, 숫자 조합 한글×)을 사용해도 되나 그 위치와 이름을 정확히 기억하자 )로 만들어 둔다. 아래 그림에서도 **STM32CubeIDEworkspace_2.2.0**폴더가 있는 위치에 **STM32CubeProjects** 폴더가 만들어져 있는 것을 확인할 수 있다.

![](./img/stm32cubemx_workspace_folder.png)



이제 **Project Manager** 탭을 클릭한다. 

![](./img/stm32cubemx_run_project_manager.png)



아래와 같이 Project Manager 화면이 열린다.

![](./img/stm32cubemx_project_manager.png)

**1. Project Location** : [Browse]버튼을 클릭하여 앞서 **STM32CubeMX**에서 생성한 프로젝트들을 저장하기위해 만들어 둔 **STM32CubeProjects** 폴더를 지정한다. 이 작업이 선행되어야 다음 단계에서 입력한 **Project Name**과 같은 이름의 폴더가 이 위치에 생성될 수 있다.

**2. Project Name** :프로젝트 이름을 영문, 숫자 조합으로 작성(한글×)한다.

**3. Toolchain / IDE** : STM32CubeIDE를 선택한다.( **매우 중요함.** 잘못 지정되어 있을 경우 **STM32CubeIDE**에서 프로젝트가 열리지 않는다. )

**4. GENERATE CODE**를 클릭한다.

![](./img/stm32cubemx_run_generate_code.png)

<img src="./img/stm32cubemx_code_generation_success.png" style="zoom:67%;" />

위 The Code is successfully generated... 팝업 메세지 창에서 **[ Open Project ]** 를 클릭하면 Project Manager에서 Toolchain / IDE로 지정한 **STM32CubeIDE**가 자동 실행되며 해당 프로젝트가 **STM32CubeIDE**의 워크스페이스에 성공적으로 Import되었다는 팝업과 함께 Project Explore에 해당 프로젝트가 열린다.

<img src="./img/stm32cubeide_import_project_complete.png" style="zoom:80%;" />

![](./img/stm32cubeide_project_explorer_after_import_project.png)



**Project Explorer**에서 **Blink** > **Core** > **Src** > **main.c** 순서로 각 항목을 확장시켜 **main.c**를 연다.

![](./img/stm32cubeide_project_explorer_project_main.png)



**STM32CubeIDE** 의 **Project**메뉴의 **Build Project**항목을 클릭하여 테스트 빌드를 수행한다.

![](./img/![](./img/stm32cubeide_project_explore_build_project.png)



다음은 **STM32CubeMX**에서 **Buzzer**프로젝트에 대해 자동 생성한 **main.c**의 내용이다.

```c
/* USER CODE BEGIN Header */
/**
  ******************************************************************************
  * @file           : main.c
  * @brief          : Main program body
  ******************************************************************************
  * @attention
  *
  * Copyright (c) 2026 STMicroelectronics.
  * All rights reserved.
  *
  * This software is licensed under terms that can be found in the LICENSE file
  * in the root directory of this software component.
  * If no LICENSE file comes with this software, it is provided AS-IS.
  *
  ******************************************************************************
  */
/* USER CODE END Header */
/* Includes ------------------------------------------------------------------*/
#include "main.h"

/* Private includes ----------------------------------------------------------*/
/* USER CODE BEGIN Includes */

/* USER CODE END Includes */

/* Private typedef -----------------------------------------------------------*/
/* USER CODE BEGIN PTD */

/* USER CODE END PTD */

/* Private define ------------------------------------------------------------*/
/* USER CODE BEGIN PD */

/* USER CODE END PD */

/* Private macro -------------------------------------------------------------*/
/* USER CODE BEGIN PM */

/* USER CODE END PM */

/* Private variables ---------------------------------------------------------*/
TIM_HandleTypeDef htim3;

UART_HandleTypeDef huart2;

/* USER CODE BEGIN PV */

/* USER CODE END PV */

/* Private function prototypes -----------------------------------------------*/
void SystemClock_Config(void);
static void MX_GPIO_Init(void);
static void MX_TIM3_Init(void);
static void MX_USART2_UART_Init(void);
/* USER CODE BEGIN PFP */

/* USER CODE END PFP */

/* Private user code ---------------------------------------------------------*/
/* USER CODE BEGIN 0 */

/* USER CODE END 0 */

/**
  * @brief  The application entry point.
  * @retval int
  */
int main(void)
{

  /* USER CODE BEGIN 1 */

  /* USER CODE END 1 */

  /* MCU Configuration--------------------------------------------------------*/

  /* Reset of all peripherals, Initializes the Flash interface and the Systick. */
  HAL_Init();

  /* USER CODE BEGIN Init */

  /* USER CODE END Init */

  /* Configure the system clock */
  SystemClock_Config();

  /* USER CODE BEGIN SysInit */

  /* USER CODE END SysInit */

  /* Initialize all configured peripherals */
  MX_GPIO_Init();
  MX_TIM3_Init();
  MX_USART2_UART_Init();
  /* USER CODE BEGIN 2 */

  /* USER CODE END 2 */

  /* Infinite loop */
  /* USER CODE BEGIN WHILE */
  while (1)
  {
    /* USER CODE END WHILE */

    /* USER CODE BEGIN 3 */
  }
  /* USER CODE END 3 */
}

/**
  * @brief System Clock Configuration
  * @retval None
  */
void SystemClock_Config(void)
{
  RCC_OscInitTypeDef RCC_OscInitStruct = {0};
  RCC_ClkInitTypeDef RCC_ClkInitStruct = {0};

  /** Initializes the RCC Oscillators according to the specified parameters
  * in the RCC_OscInitTypeDef structure.
  */
  RCC_OscInitStruct.OscillatorType = RCC_OSCILLATORTYPE_HSI;
  RCC_OscInitStruct.HSIState = RCC_HSI_ON;
  RCC_OscInitStruct.HSICalibrationValue = RCC_HSICALIBRATION_DEFAULT;
  RCC_OscInitStruct.PLL.PLLState = RCC_PLL_ON;
  RCC_OscInitStruct.PLL.PLLSource = RCC_PLLSOURCE_HSI_DIV2;
  RCC_OscInitStruct.PLL.PLLMUL = RCC_PLL_MUL16;
  if (HAL_RCC_OscConfig(&RCC_OscInitStruct) != HAL_OK)
  {
    Error_Handler();
  }

  /** Initializes the CPU, AHB and APB buses clocks
  */
  RCC_ClkInitStruct.ClockType = RCC_CLOCKTYPE_HCLK|RCC_CLOCKTYPE_SYSCLK
                              |RCC_CLOCKTYPE_PCLK1|RCC_CLOCKTYPE_PCLK2;
  RCC_ClkInitStruct.SYSCLKSource = RCC_SYSCLKSOURCE_PLLCLK;
  RCC_ClkInitStruct.AHBCLKDivider = RCC_SYSCLK_DIV1;
  RCC_ClkInitStruct.APB1CLKDivider = RCC_HCLK_DIV2;
  RCC_ClkInitStruct.APB2CLKDivider = RCC_HCLK_DIV1;

  if (HAL_RCC_ClockConfig(&RCC_ClkInitStruct, FLASH_LATENCY_2) != HAL_OK)
  {
    Error_Handler();
  }
}

/**
  * @brief TIM3 Initialization Function
  * @param None
  * @retval None
  */
static void MX_TIM3_Init(void)
{

  /* USER CODE BEGIN TIM3_Init 0 */

  /* USER CODE END TIM3_Init 0 */

  TIM_ClockConfigTypeDef sClockSourceConfig = {0};
  TIM_MasterConfigTypeDef sMasterConfig = {0};
  TIM_OC_InitTypeDef sConfigOC = {0};

  /* USER CODE BEGIN TIM3_Init 1 */

  /* USER CODE END TIM3_Init 1 */
  htim3.Instance = TIM3;
  htim3.Init.Prescaler = 64-1;
  htim3.Init.CounterMode = TIM_COUNTERMODE_UP;
  htim3.Init.Period = 65535;
  htim3.Init.ClockDivision = TIM_CLOCKDIVISION_DIV1;
  htim3.Init.AutoReloadPreload = TIM_AUTORELOAD_PRELOAD_DISABLE;
  if (HAL_TIM_Base_Init(&htim3) != HAL_OK)
  {
    Error_Handler();
  }
  sClockSourceConfig.ClockSource = TIM_CLOCKSOURCE_INTERNAL;
  if (HAL_TIM_ConfigClockSource(&htim3, &sClockSourceConfig) != HAL_OK)
  {
    Error_Handler();
  }
  if (HAL_TIM_PWM_Init(&htim3) != HAL_OK)
  {
    Error_Handler();
  }
  sMasterConfig.MasterOutputTrigger = TIM_TRGO_RESET;
  sMasterConfig.MasterSlaveMode = TIM_MASTERSLAVEMODE_DISABLE;
  if (HAL_TIMEx_MasterConfigSynchronization(&htim3, &sMasterConfig) != HAL_OK)
  {
    Error_Handler();
  }
  sConfigOC.OCMode = TIM_OCMODE_PWM1;
  sConfigOC.Pulse = 0;
  sConfigOC.OCPolarity = TIM_OCPOLARITY_HIGH;
  sConfigOC.OCFastMode = TIM_OCFAST_DISABLE;
  if (HAL_TIM_PWM_ConfigChannel(&htim3, &sConfigOC, TIM_CHANNEL_2) != HAL_OK)
  {
    Error_Handler();
  }
  /* USER CODE BEGIN TIM3_Init 2 */

  /* USER CODE END TIM3_Init 2 */
  HAL_TIM_MspPostInit(&htim3);

}

/**
  * @brief USART2 Initialization Function
  * @param None
  * @retval None
  */
static void MX_USART2_UART_Init(void)
{

  /* USER CODE BEGIN USART2_Init 0 */

  /* USER CODE END USART2_Init 0 */

  /* USER CODE BEGIN USART2_Init 1 */

  /* USER CODE END USART2_Init 1 */
  huart2.Instance = USART2;
  huart2.Init.BaudRate = 115200;
  huart2.Init.WordLength = UART_WORDLENGTH_8B;
  huart2.Init.StopBits = UART_STOPBITS_1;
  huart2.Init.Parity = UART_PARITY_NONE;
  huart2.Init.Mode = UART_MODE_TX_RX;
  huart2.Init.HwFlowCtl = UART_HWCONTROL_NONE;
  huart2.Init.OverSampling = UART_OVERSAMPLING_16;
  if (HAL_UART_Init(&huart2) != HAL_OK)
  {
    Error_Handler();
  }
  /* USER CODE BEGIN USART2_Init 2 */

  /* USER CODE END USART2_Init 2 */

}

/**
  * @brief GPIO Initialization Function
  * @param None
  * @retval None
  */
static void MX_GPIO_Init(void)
{
  GPIO_InitTypeDef GPIO_InitStruct = {0};
  /* USER CODE BEGIN MX_GPIO_Init_1 */

  /* USER CODE END MX_GPIO_Init_1 */

  /* GPIO Ports Clock Enable */
  __HAL_RCC_GPIOC_CLK_ENABLE();
  __HAL_RCC_GPIOD_CLK_ENABLE();
  __HAL_RCC_GPIOA_CLK_ENABLE();
  __HAL_RCC_GPIOB_CLK_ENABLE();

  /*Configure GPIO pin Output Level */
  HAL_GPIO_WritePin(LD2_GPIO_Port, LD2_Pin, GPIO_PIN_RESET);

  /*Configure GPIO pin : B1_Pin */
  GPIO_InitStruct.Pin = B1_Pin;
  GPIO_InitStruct.Mode = GPIO_MODE_IT_RISING;
  GPIO_InitStruct.Pull = GPIO_NOPULL;
  HAL_GPIO_Init(B1_GPIO_Port, &GPIO_InitStruct);

  /*Configure GPIO pin : LD2_Pin */
  GPIO_InitStruct.Pin = LD2_Pin;
  GPIO_InitStruct.Mode = GPIO_MODE_OUTPUT_PP;
  GPIO_InitStruct.Pull = GPIO_NOPULL;
  GPIO_InitStruct.Speed = GPIO_SPEED_FREQ_LOW;
  HAL_GPIO_Init(LD2_GPIO_Port, &GPIO_InitStruct);

  /* EXTI interrupt init*/
  HAL_NVIC_SetPriority(EXTI15_10_IRQn, 0, 0);
  HAL_NVIC_EnableIRQ(EXTI15_10_IRQn);

  /* USER CODE BEGIN MX_GPIO_Init_2 */

  /* USER CODE END MX_GPIO_Init_2 */
}

/* USER CODE BEGIN 4 */

/* USER CODE END 4 */

/**
  * @brief  This function is executed in case of error occurrence.
  * @retval None
  */
void Error_Handler(void)
{
  /* USER CODE BEGIN Error_Handler_Debug */
  /* User can add his own implementation to report the HAL error return state */
  __disable_irq();
  while (1)
  {
  }
  /* USER CODE END Error_Handler_Debug */
}
#ifdef USE_FULL_ASSERT
/**
  * @brief  Reports the name of the source file and the source line number
  *         where the assert_param error has occurred.
  * @param  file: pointer to the source file name
  * @param  line: assert_param error line source number
  * @retval None
  */
void assert_failed(uint8_t *file, uint32_t line)
{
  /* USER CODE BEGIN 6 */
  /* User can add his own implementation to report the file name and line number,
     ex: printf("Wrong parameters value: file %s on line %d\r\n", file, line) */
  /* USER CODE END 6 */
}
#endif /* USE_FULL_ASSERT */

```

지금 구현하려는 기능은 **NUCLEO-F103RB**보드의 **PA9**에 연결한 Buzzer를 통해 도, 레, 미, 파, 솔, 라, 시, 도 음계를 출력하는 것이다. 이를 위해 필요한 HAL(Hardware Abstract Layer:하드웨어 추상화 계층) 라이브러리는 , `HAL_TIM_PWM_Start()`, `HAL_TIM_PWM_Stop()`, `__HAL_TIM_SET_AUTORELOAD()`, `__HAL_TIM_SET_COMPARE()`, 

`HAL_GPIO_WritePin()`함수원형은 아래와 같다.

```c
void HAL_GPIO_WritePin(
    GPIO_TypeDef *GPIOx,
    uint16_t GPIO_Pin,
    GPIO_PinState PinState
);
```

`HAL_GPIO_WritePin()`함수의 매개변수와 의미는 다음과 같다.

| 매개변수   | 의미                                |
| ---------- | ----------------------------------- |
| `GPIOx`    | 사용할 GPIO 포트                    |
| `GPIO_Pin` | 제어할 GPIO 핀                      |
| `PinState` | 핀에 출력할 값 (`SET` 또는 `RESET`) |



`HAL_Delay()`함수원형은 아래와 같다.

```c
void HAL_Delay(uint32_t Delay);
```

`HAL_Delay()`함수의 매개변수와 의미는 다음과 같다.

| 매개변수   | 의미                                |
| ---------- | ----------------------------------- |
| `Delay`    | 지연할 시간. 단위는 **ms(밀리초)**  |



`main.c`의 47~49행의 다음 코드를 찾는다.

```c
/* USER CODE BEGIN PV */

/* USER CODE END PV */

```



위코드를 다음과 같이 수정 편집 후 저장한다.

```c
/* USER CODE BEGIN PV */
uint16_t note[8] = {262, 294, 330, 349, 392, 440, 494, 523};
/* USER CODE END PV */
```





`main.c`의 61~63행의 다음 코드를 찾는다.

```c
/* USER CODE BEGIN 0 */

/* USER CODE END 0 */

```



위코드를 다음과 같이 수정 편집 후 저장한다.

```c
/* USER CODE BEGIN 0 */
 void Buzzer_Tone(uint16_t frequency, uint16_t duration)
{
    uint32_t period;

    if (frequency == 0)
    {
        HAL_TIM_PWM_Stop(&htim3, TIM_CHANNEL_2);
        HAL_Delay(duration);
        return;
    }

    /* TIM1 counter clock = 1 MHz */
    period = 1000000 / frequency;

    /* Set PWM frequency */
    __HAL_TIM_SET_AUTORELOAD(&htim3, period - 1);

    /* 50% duty cycle */
    __HAL_TIM_SET_COMPARE(&htim3, TIM_CHANNEL_2, period / 2);

    /* Reset counter */
    __HAL_TIM_SET_COUNTER(&htim3, 0);

    /* Start PWM */
    HAL_TIM_PWM_Start(&htim3, TIM_CHANNEL_2);

    HAL_Delay(duration);

    /* Stop sound */
    HAL_TIM_PWM_Stop(&htim3, TIM_CHANNEL_2);
}
/* USER CODE END 0 */
```





`main.c`의 126~128행의 다음 코드를 찾는다.

```c
 /* USER CODE BEGIN 2 */

  /* USER CODE END 2 */

```



위코드를 다음과 같이 수정 편집 후 저장한다.

```c
/* USER CODE BEGIN 2 */
for (int i = 0; i < 8; i++)
{
    Buzzer_Tone(note[i], 500);
    HAL_Delay(100);
}
  /* USER CODE END 2 */
```





**STM32CubeIDE**의 **Project** 메뉴의 **Build Project** 항목을 클릭하여 프로젝트를 빌드한다. 

![](./img/![](./img/stm32cubeide_project_explore_build_project.png)



이제 앞서 빌드한 결과를 타겟보드에 올려 동작 시켜보자. **STM32CubeIDE**의 **Run**메뉴의 **Run**항목을 클릭한다.

![](./img/stm32cubeide_project_explorer_run_run.png)

이제 **NUCLEO-F103RB** 타겟보드의 검은색 리셋 스위치를 누를 때 마다 **PC7**에 연결한 Buzzer를 통해 도, 레, 미, 파, 솔, 라, 시, 도 음계가 재생되는 것을 확인한다. 





[**목차**](../../README.md) 
