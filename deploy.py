with open("./simplestorage.sol","r")as file;
  simple_storeage_file =file.read()
print(simple_storeage_file)
compiled_sol =compled-standard{
{
  "language"; "Solidity",
"sources": {"SimpleStorage.sol": {"content": simple_storage_file}},
"settings": {
  "outputSelection":{
    "*":{"*": ["abc","metdata","evm.bytecode","evm.sourceMap"]}
  }
  },
},
soll_veersion="0.6.0"
}
print(compiled_sol)
