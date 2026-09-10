## STM32Cube를 이용한 STM32 프로그래밍

### LED Blink

**STM32CubeMX**와 **STM32CubeIDE**를 이용하여  **NUCLEO-F103RB**보드의 온 보드 **LED**를 0.5초동안 점등 후, 0.5초동안 소등을 무한 반복하는 **LED Blink**를 구현해 보자.  

##### 개발 환경

**OS: ** **MS Windows11**

**타겟보드: ** **NUCLEO-F103RB**

**SW Tools: ** **[STM32CubeMX 6.18.1](https://www.st.com/en/development-tools/stm32cubemx.html)** / **[STM32CubeIDE 2.20](https://www.st.com/en/development-tools/stm32cubeide.html)**

---

**CubeMX에서 설정할 Peripheral**

​	**RCC **의  클럭 소스만 설정 하고 나머지 **Peripheral**은 기본값으로 설정(따로 설정하지 않는다. ) 

새로운 STM32 프로젝트 생성을 위해 STM32CubeMX 실행 후, 타겟 설정을 위해 **ACCESS TO BOARD SELECTOR**를 클릭한다.

![](./img/stm32cubemx_select_target1.png)

New Project from Board 화면의 **PRODUCT INFO**의 **Type**에서 **Nucleo-64**를 체크한다. 

![](./img/stm32cubemx_select_target2.png)

New Project fron Board 화면의 **PRODUCT INFO**를 스크롤다운해서 **MCU/MPU Series**에서 **STM32F1**을 체크하면 화면 우측의 **Board List**가 확 줄어든 것을 볼 수 있다. 그 중에서 타겟보드로 사용중인 **NUCLEO-F103RB**를 선택 후 화면 오른쪽 상단의 **Start Project**를 클릭한다.



![](./img/stm32cubemx_start_project.png)



![](./img/init_all_periperals_with_default.png)

위 모든 주변장치들을 기본 모드로 초기화 하겠냐는 팝업창에서 **[  <u>Y</u>es  ]**를 클릭하면

**GPIO** **PA5**는 Output Push pull로,  **PC13**은 External Interrupt Mode with Rising edge trigger detection으로 설정되고

**USART2**는 **Baudrate**115200,  **Parity** none, **Data** 8bit, **Stop** 1bit가 **default**(기본값)으로 설정된다.



최우선으로 설정해야 하는 것은 **RCC** 설정이다. **Pinout & Configuration**탭에서 **System Core**를 선택 후,  **RCC**를 클릭하고 바로 우측의 RCC Mode and Configuration의 Mode에서 High Speed Clock(HSE)와 Low Speed Clock(LSE)를 모두 Disable로 설정한다. 이는 모든 외부 클럭을 Disable시킨 것으로 **HSI**(High Speed Internal Clock)를 클럭 소스로 사용하겠다는 의미이다.

![](./img/stm32cubemx_rcc_config.png)

CLOCK설정 확인을 위해 **Clock Configuration**탭을 클릭하여 최초 **HSI**(High Speed Internal Clock) 8MHz를 소스 클럭으로 시작하여 64MHz의 시스템 클럭으로 공급되는 것을 확인한다.

![](./img/stm32cubemx_check_clock.png)



다음은 **Initialize all peripheral with their default Mode ?**팝업 창에서 **[ <u>Y</u>es ]**를 클릭한 경우의 **GPIO** 설정상태이다.

![](./img/stm32cubemx_gpio_default_config.png)

다음 역시 **Initialize all peripheral with their default Mode ?**팝업 창에서 **[ <u>Y</u>es ]**를 클릭한 경우의 **USART2** 설정상태이다.

![](./img/stm32cubemx_usart2_default_config.png)



여기까지 설정을 반영한 코드 생성을위해 **Generate Code**를 클릭 하기 전 **STM32CubeMX**에서 생성한 프로젝트들을 저장해 둘 폴더를 만들어 두어야 한다. 그 위치는 편의상 **STM32CubeIDEworkspace_2.2.0** 폴더와 같은 폴더에, 폴더 이름은 **STM32CubeProjects**(폴더 이름은 다른 임의의이름(영문, 숫자 조합 한글×)을 사용해도 되나 그 위치와 이름을 정확히 기억하자 )로 만들어 둔다. 아래 그림에서도 **STM32CubeIDEworkspace_2.2.0**폴더가 있는 위치에 **STM32CubeProjects** 폴더가 만들어져 있는 것을 확인할 수 있다.

![](./img/stm32cubemx_workspace_folder.png)



이제 **Project Manager** 탭을 클릭한다. 

![](./img/stm32cubemx_run_project_manager.png)



아래와 같이 Project Manager 화면이 열린다.

![](./img/stm32cubemx_project_manager.png)

**1. Project Location** : [Browse]버튼을 클릭하여 앞서 **STM32CubeMX**에서 생성한 프로젝트들을 저장하기위해 만들어 둔 **STM32CubeProjects** 폴더를 지정한다. 이 작업이 선행되어야 다음 단계에서 입력한 **Project Name**과 같은 이름의 폴더가 이 위치에 생성될 수 있다.

**2. Project Name** :프로젝트 이름을 영문, 숫자 조합으로 작성(한글×)한다.

**3. Toolchain / IDE** : STM32CubeIDE를 선택한다.( **<u>매우 중요함.</u>** 잘못 지정되어 있을 경우 **STM32CubeIDE**에서 프로젝트가 열리지 않는다. )

**4. GENERATE CODE**를 클릭한다.

![](./img/stm32cubemx_run_generate_code.png)

<img src="./img/stm32cubemx_code_generation_success.png" style="zoom:67%;" />

위 The Code is successfully generated... 팝업 메세지 창에서 **[ Open Project]** 를 클릭하면 Project Manager에서 Toolchain / IDE로 지정한 **STM32CubeIDE**가 자동 실행되며 다음 팝업과 함께 Project Explore에 해당 프로젝트가 로딩된다.

<img src="./img/stm32cubeide_import_project_complete.png" style="zoom:80%;" />

![](./img/stm32cubeide_project_explorer_after_import_project.png)



**Project Explorer**에서 **Sample** > **Core** > **Src** > **main.c** 순서로 각 항목을 확장시켜 **main.c**를 연다.

![](./img/stm32cubeide_project_explorer_project_main.png)



**STM32CubeIDE** 의 **<u>P</u>roject**메뉴의 **Build Project**항목을 클릭하여 테스트 빌드를 수행한다.

![](./img/![](./img/stm32cubeide_project_explore_build_project.png)



다음은 **STM32CubeMX**에서 **ToggleLED**프로젝트에 대해 자동 생성한 **main.c**의 내용이다.

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
UART_HandleTypeDef huart2;

/* USER CODE BEGIN PV */

/* USER CODE END PV */

/* Private function prototypes -----------------------------------------------*/
void SystemClock_Config(void);
static void MX_GPIO_Init(void);
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
  HAL_GPIO_WritePin(GPIOA, GPIO_PIN_5, GPIO_PIN_RESET);

  /*Configure GPIO pin : PC13 */
  GPIO_InitStruct.Pin = GPIO_PIN_13;
  GPIO_InitStruct.Mode = GPIO_MODE_INPUT;
  GPIO_InitStruct.Pull = GPIO_PULLUP;
  HAL_GPIO_Init(GPIOC, &GPIO_InitStruct);

  /*Configure GPIO pin : PA5 */
  GPIO_InitStruct.Pin = GPIO_PIN_5;
  GPIO_InitStruct.Mode = GPIO_MODE_OUTPUT_PP;
  GPIO_InitStruct.Pull = GPIO_NOPULL;
  GPIO_InitStruct.Speed = GPIO_SPEED_FREQ_LOW;
  HAL_GPIO_Init(GPIOA, &GPIO_InitStruct);

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

지금 구현하려는 기능은 **NUCLEO-F103RB**타겟보드와 PC를 USB 케이블로 연결하고 PC에서 실행한 시리얼 통신 에뮬레이터 프로그램(TERATERM, Putty 등)을 통해 '1'을 수신하면 온보드 LED를 켜고, '0'을 수신하면 온보드 LED를 끄는 것이다. 이를 위해 필요한 HAL(Hardware Abstract Layer:하드웨어 추상화 계층) 라이브러리는 **USART**로부터 임의의 크기의 문자열을 수신하는 **`HAL_UART_Receive()`**와 임의의 **GPIO Pin**으로 신호를 출력하는 **`HAL_GPIO_WritePin()`** 2가지이다.

**`HAL_UART_Receive()`**함수원형은 아래와 같다.

```c
HAL_StatusTypeDef HAL_UART_Receive(
    UART_HandleTypeDef *huart,
    uint8_t *pData,
    uint16_t Size,
    uint32_t Timeout
);
```

**`HAL_UART_Receive()`**함수의 매개변수와 의미는 다음과 같다.


| 매개변수  | 의미                               |
| --------- | ---------------------------------- |
| `huart`   | 사용할 UART의 핸들 주소            |
| `pData`   | 수신한 데이터를 저장할 버퍼의 주소 |
| `Size`    | 수신할 데이터의 개수(byte)         |
| `Timeout` | 수신을 기다릴 최대 시간(ms)        |



**`HAL_GPIO_WritePin()`**함수원형은 아래와 같다.

```c
void HAL_GPIO_WritePin(
    GPIO_TypeDef *GPIOx,
    uint16_t GPIO_Pin,
    GPIO_PinState PinState
);
```

**`HAL_GPIO_WritePin()`**함수의 매개변수와 의미는 다음과 같다.

| 매개변수   | 의미                                |
| ---------- | ----------------------------------- |
| `GPIOx`    | 사용할 GPIO 포트                    |
| `GPIO_Pin` | 제어할 GPIO 핀                      |
| `PinState` | 핀에 출력할 값 (`SET` 또는 `RESET`) |



`main.c`의 44~46행의 다음 코드를 찾는다.

```c
/* USER CODE BEGIN PV */

/* USER CODE END PV */

```



위코드를 다음과 같이 수정 편집 후 저장한다.

```c
/* USER CODE BEGIN PV */
uint8_t ch = 0;
/* USER CODE END PV */
```



`main.c`의 98~101행의 다음 코드를 찾는다.

```c
/* USER CODE BEGIN WHILE */
  while (1)
  {
    /* USER CODE END WHILE */

```



위코드를 다음과 같이 수정 편집 후 저장한다.

```c
/* USER CODE BEGIN WHILE */
  while (1)
  {
	  HAL_UART_Receive(&huart2, &ch, sizeof(ch), 10);
	  if(ch == '1')
	  {
		  HAL_GPIO_WritePin(GPIOA, GPIO_PIN_5, 1);
	  }
	  else if(ch == '0')
	  {
		  HAL_GPIO_WritePin(GPIOA, GPIO_PIN_5, 0);
	  }
	  else;
    /* USER CODE END WHILE */
```



**STM32CubeIDE**의 **Project** 메뉴의 **Build Project** 항목을 클릭하여 프로젝트를 빌드한다. 



빌드 결과는 **ST-Link**를 통해 타겟보드에 업로드 해야 하므로 그 전에  **ST-Link**의 펌웨어를 업그레이드 하기 위해 **<u>H</u>elp**메뉴의 **ST-Link Upgrade**항목을 클릭한다.

![](./img\st_link_upgrade1.png)

[ Open in update mode ] 버튼을 클릭한다.

![](./img\st_link_upgrade2.png)

[ Open in update mode ] 를 클릭 하면 Unknown으로  표시되던 Current Firmware Type 및 Version, Update to Firmware 정보가 표시된다. 이 때 [Upgrade] 버튼을 클릭한다.

![](./img\st_link_upgrade3.png)

업그레이드 진행상태가 표시된다.

![](./img\st_link_upgrade4.png)



업그레이드가 완료되면 Upgrade sucessful. 메세지가 나타난다.

![](./img\st_link_upgrade5.png)

새로운 **ST-Link** 펌웨어가 나오지 않는 한 더 이상의 업데이트는  필요 없다. 이제 앞서 빌드한 결과를 타겟보드에 올려 동작 시켜보자. **STM32CubeIDE**의 **<u>R</u>UN**메뉴의 **Run**항목을 클릭한다.

![](./img/stm32cubeide_run_run.png)



이제 **NUCLEO-F103RB** 타겟보드의 검은색 리셋 스위치 아래 녹색 LED(LED2)가 0.5초동안 켜졌다, 다시 0.5초동안 꺼졌다를 반복하는 것을 확인한다.





[**목차**](../../README.md) 
