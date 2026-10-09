# 10-Bit Single-Cycle Processor Design

A custom 10-bit single-cycle processor designed and simulated using the **Digital** logic simulator for the Computer Architecture course at Sharif University of Technology.

This repository contains the hardware schematic design, custom Instruction Set Architecture (ISA) specifications, and an assembly program implementing a battery charge/discharge control algorithm.

---

## 📌 Project Overview

The objective of this project is to design a simple single-cycle processor from scratch and demonstrate its capability to execute a multi-step control program automatically using a custom instruction set.

- **Course**: Computer Architecture 
- **Institution**: Sharif University of Technology – Department of Electrical Engineering
- **Instructor**: Dr. Saeed Bagheri Shourki
- **Simulator**: [Digital Logic Simulator](https://github.com/hneemann/Digital)

---

## 👨‍💻 Author

- **Mohammadmehdi Fotouhi Firouzabad**  
  - Electrical Engineering Student, Sharif University of Technology  

---

## 🏗️ Hardware Architecture & Datapath

The processor features a 10-bit data and instruction width with the following components:

1. **Program Counter (PC)**: A counter tracking instruction memory addresses. Supports sequential execution and conditional jumps.
2. **Instruction Memory (ROM)**: Stores the 10-bit machine code instructions.
3. **Register File**: 16 internal 10-bit registers ($R_0$ to $R_{15}$) with 4-bit addressing (2 read ports, 1 write port).
4. **Arithmetic Logic Unit (ALU)**: Executes addition, subtraction, and comparison operations.
5. **Control Unit & Multiplexers**: Decodes instruction opcodes and routes control signals across the datapath.
6. **7-Segment Display Output**: Displays the battery charging status during execution.

---

## 📜 Instruction Set Architecture (ISA)

The processor uses a custom 10-bit instruction format:

| Instruction | Syntax | Opcode / Format | Description |
| :--- | :--- | :--- | :--- |
| **IMM** | `IMM Val` | `01` + 8-bit Value | Loads an 8-bit immediate value into register $R_5$ (zero-extended) |
| **MOV** | `MOV Rs, Rd` | `10` + $R_s$ (4b) + $R_d$ (4b) | Copies data from source register $R_s$ to destination register $R_d$ |
| **ADD** | `ADD Rd` | `11` + `0000` + $R_d$ (4b) | Calculates $R_d = R_0 + R_1$ |
| **SUB** | `SUB Rd` | `11` + `0001` + $R_d$ (4b) | Calculates $R_d = R_0 - R_1$ |
| **CND** | `CND Target` | `00` + 8-bit Target Address | Compares operands; updates $PC = \text{Target}$ if the condition is met |

---

## 🔋 Test Program: Battery Charge Controller

To demonstrate processor execution, an assembly program was written to control a battery charge cycle:

- **Initial State**: Battery level starts at 80 units.
- **Discharge Mode**: Decreases charge level by 4 units per step.
- **Threshold**: When charge drops below 20 units, charging mode triggers.
- **Charge Mode**: Increases charge by 6 units per step and turns ON the 7-segment display indicator.
- **Completion**: Once charge reaches 90 units, charging turns OFF, and normal discharge resumes.

---

## 🚀 How to Run the Simulation

Follow these steps to run the processor in the **Digital** logic simulator:

1. **Prerequisites**:
   - Download and install the [Digital Logic Simulator](https://github.com/hneemann/Digital).
   - Ensure Java (JRE 8 or higher) is installed on your machine.

2. **Assembly & Machine Code Generation**:
   - If you modify `asm/ev_controller.asm`, convert the binary/assembly sequence into HEX format using the provided Python utility:
     ```bash
     python tools/assembler.py
     ```
   - Alternatively, use the pre-generated `asm/ev_controller.hex`.

3. **Running in Simulator**:
   - Launch **Digital** and open `src/main_processor.dig`.
   - Right-click on the **ROM (Instruction Memory)** component in the circuit.
   - Click **Edit**, select **Load**, and choose the `asm/ev_controller.hex` file.
   - Click the **Play/Start** button (or press `Ctrl + M`) to start the simulation clock.
   - Observe the execution: monitor the `PC` updates, register contents inside the Register File, and the status of the 7-segment display for battery charge indication.

---

## 📁 Repository Structure

```text
.
├── docs/               # Block diagrams and simulation screenshots
├── src/                # Circuit files (.dig) for Digital simulator
├── asm/                # Assembly source code and generated HEX file
├── tools/              # Python conversion script (Assembly/Binary to HEX)
└── README.md           # Project documentation
