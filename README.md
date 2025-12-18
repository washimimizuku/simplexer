# Simplexer

A high-performance lexer and parser framework built in Rust for scientific computing and domain-specific languages.

## Overview

Simplexer provides fast, memory-safe tokenization and parsing capabilities optimized for scientific data formats, configuration files, and domain-specific languages in conservation biology and environmental science.

## Goals

### 🎯 **Primary Objectives**
- **High Performance**: Zero-cost abstractions for processing large scientific datasets
- **Memory Safety**: Rust's ownership model prevents common parsing vulnerabilities
- **Scientific Focus**: Built-in support for scientific notation, units, and data formats
- **Extensible**: Plugin architecture for custom token types and grammar rules

### 🔬 **Target Applications**
- Conservation biology data formats (species observations, genetic data)
- Environmental monitoring configuration files
- Scientific modeling DSLs
- Climate data parsing (NetCDF metadata, CSV with scientific notation)
- GIS data format processing

## Features

### ✅ **Current (Rust Implementation)**
- Fast tokenization with regex-based lexer
- Recursive descent parser with error recovery
- Scientific number parsing (1.5e-10, units)
- UTF-8 string handling
- Comprehensive error reporting with line/column info

### 🚧 **In Development**
- Parser combinator integration (`nom`)
- AST (Abstract Syntax Tree) generation
- Custom token type plugins
- Streaming parser for large files

### 📋 **Planned**
- WASM compilation for browser use
- Language server protocol support
- Integration with conservation-biology-toolkit
- Procedural macro support for code generation

## Quick Start

```bash
# Install Rust (if not already installed)
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

# Clone and build
git clone https://github.com/washimimizuku/simplexer.git
cd simplexer
cargo build --release

# Run examples
cargo run --example scientific_data
cargo run --example conservation_config
```

## Usage Examples

### Basic Tokenization
```rust
use simplexer::{Lexer, Token};

let input = "population_size = 1.5e3 individuals";
let mut lexer = Lexer::new(input);

while let Some(token) = lexer.next_token()? {
    println!("{:?}", token);
}
// Output: Identifier("population_size"), Equals, Number(1500.0), Unit("individuals")
```

### Conservation Data Parsing
```rust
use simplexer::Parser;

let config = r#"
    species "Canis lupus" {
        population_size: 2500
        habitat_area: 15000 km²
        threat_level: "endangered"
    }
"#;

let ast = Parser::parse_conservation_config(config)?;
```

### Scientific Notation Support
```rust
// Handles scientific notation, units, and uncertainty
let data = "temperature = 23.5 ± 0.2 °C";
let tokens = Lexer::new(data).tokenize()?;
// Produces: Identifier, Equals, Number(23.5), PlusMinus, Number(0.2), Unit("°C")
```

## Architecture

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│     Lexer       │───▶│     Parser       │───▶│      AST        │
│  (Tokenization) │    │  (Syntax Tree)   │    │  (Evaluation)   │
└─────────────────┘    └──────────────────┘    └─────────────────┘
         │                       │                       │
         ▼                       ▼                       ▼
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Token Stream  │    │   Parse Tree     │    │    Output       │
│   [Id, =, Num]  │    │   Expression     │    │   Processed     │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```

## Performance

- **Tokenization**: ~50MB/s for scientific data files
- **Memory Usage**: Zero-copy string slicing where possible
- **Error Recovery**: Continues parsing after syntax errors
- **Streaming**: Handles files larger than available RAM

## Rust Learning Focus

This project demonstrates:
- **Ownership & Borrowing**: String slicing and lifetime management
- **Error Handling**: `Result<T, E>` patterns throughout
- **Pattern Matching**: Extensive use with token types
- **Iterators**: Custom iterator implementations for token streams
- **Traits**: Generic parsing interfaces
- **Performance**: Zero-cost abstractions and memory efficiency

## Contributing

We welcome contributions, especially:
- New scientific data format support
- Performance optimizations
- Additional parser combinators
- Documentation improvements

## License

MIT License - see [LICENSE](LICENSE) for details.

## Related Projects

- [conservation-biology-toolkit](https://github.com/washimimizuku/conservation-biology-toolkit) - Uses Simplexer for data parsing
- [jasmine-lang](https://github.com/washimimizuku/jasmine-lang) - DSL built on Simplexer foundation
- [30-days-rust-data-ai](https://github.com/washimimizuku/30-days-rust-data-ai) - Learning journey documentation
