# Domain-Specific Math LLM: Fine-tuning Qwen2.5-Math

This project focuses on domain adaptation of the Qwen2.5-Math-1.5B model through continued pretraining (CPT) on specialized research papers, preserving mathematical reasoning capabilities while introducing domain expertise.

## Project Overview

I collected and preprocessed 100 research papers related to central configurations in the n-body problem, maintaining LaTeX mathematical notation for optimal training. This specialized corpus was then used to adapt the Qwen2.5-Math-1.5B model using Parameter-Efficient Fine-Tuning (PEFT) techniques.

## Base Model: Qwen2.5-Math-1.5B

Qwen2.5-Math is a specialized mathematical language model with impressive capabilities:

- Supports both Chain-of-Thought (CoT) and Tool-integrated Reasoning (TIR)
- Handles mathematical problem-solving in both English and Chinese
- Achieves state-of-the-art performance on mathematical benchmarks
- Excels at symbolic manipulation and algorithmic reasoning

The 1.5B parameter base model variant was selected for its balance of performance and computational efficiency.

## Implementation Details

### Data Preprocessing

- Collected 100 research papers on central configurations
- Preserved LaTeX mathematical notation and equations
- Compiled into a unified corpus for training
- Tokenized and chunked into 2048-token segments


### Training Configuration

I implemented LoRA (Low-Rank Adaptation) with optimized parameters for continued pretraining:

```python
# LoRA configuration with targeted parameter efficiency
lora_config = LoraConfig(
    r=8,                            # Rank parameter
    lora_alpha=16,                  # Scaling factor
    target_modules=[                # Targeted model components
        "q_proj", "k_proj", "v_proj", "o_proj", 
        "gate_proj", "up_proj", "down_proj", "wte", "lm_head"
    ],
    lora_dropout=0.05,
    bias="none",
    task_type=TaskType.CAUSAL_LM,
)

# Training arguments optimized for efficient learning
training_args = TrainingArguments(
    output_dir="./qwen_math_nbody_lora",
    num_train_epochs=3,
    per_device_train_batch_size=1,
    gradient_accumulation_steps=16,
    learning_rate=1e-4,
    weight_decay=0.01,
    fp16=True,
    gradient_checkpointing=True,
    gradient_checkpointing_kwargs={"use_reentrant": False},
    optim="adamw_hf"
)
```


### Advanced Techniques

- **Decoupled Learning Rates**: Implemented separate learning rates for embedding layers (1e-5) versus other parameters (1e-4)
- **Memory Optimization**: Used gradient checkpointing and FP16 precision
- **Custom Training Loop**: Created a specialized trainer with enhanced progress tracking
- **Targeted Parameter Updates**: Focused training on critical model components for efficient adaptation


## Future Directions

### Supervised Fine-Tuning (SFT)

The next phase will involve supervised fine-tuning on instruction-response pairs to enhance the model's ability to follow directions and generate coherent responses. This will transform the current completion-based model into a more conversational assistant. Steps include:

- Creating a specialized instruction dataset for mathematical research
- Implementing RLHF (Reinforcement Learning from Human Feedback) techniques
- Balancing domain expertise with instruction-following capabilities


### Prompt Engineering

Developing specialized prompting techniques for the fine-tuned model:

- Few-shot prompting for complex mathematical problems
- Chain-of-thought templates for theoretical physics applications
- Tool-calling prompts to leverage computational capabilities


### Evaluation Framework

- Implementing benchmarks specific to central configurations and n-body problems
- Comparative analysis against specialized mathematical models
- User studies with domain experts to assess practical utility


### Deployment Considerations

- Packaging the model for efficient inference
- Creating specialized APIs for research applications
- Documentation of model capabilities and limitations


## Requirements

```
transformers>=4.37.0
peft>=0.4.0
torch>=2.0.0
datasets
tqdm
```


## Citation

```
@article{yang2024qwen25mathtechnicalreportmathematical,
  title={Qwen2.5-Math Technical Report: Toward Mathematical Expert Model via Self-Improvement}, 
  author={An Yang and Beichen Zhang and Binyuan Hui and Bofei Gao and Bowen Yu and Chengpeng Li and Dayiheng Liu and Jianhong Tu and Jingren Zhou and Junyang Lin and Keming Lu and Mingfeng Xue and Runji Lin and Tianyu Liu and Xingzhang Ren and Zhenru Zhang},
  journal={arXiv preprint arXiv:2409.12122},
  year={2024}
}
```
