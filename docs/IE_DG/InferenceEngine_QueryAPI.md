Introduction to Inference Engine Device Query API {#openvino_docs_IE_DG_InferenceEngine_QueryAPI}
===============================

This section provides a high-level description of the process of querying of different device properties and configuration values.
Refer to the [Hello Query Device Sample](../../inference-engine/samples/hello_query_device/README.md) sources and [Multi-Device Plugin guide](supported_plugins/MULTI.md) for example of using the Inference Engine Query API in user applications.

## Using the Inference Engine Query API in Your Code

The Inference Engine `Core` class provides the following API to query device information, set or get different device configuration properties:

* <code>InferenceEngine::Core::GetAvailableDevices</code> - Provides a list of available devices. If there are more than one instance of a specific device, the devices are enumerated with `.suffix` where `suffix` is a unique string identifier. The device name can be passed to all methods of the `InferenceEngine::Core` class that work with devices, for example `InferenceEngine::Core::LoadNetwork`.
* <code>InferenceEngine::Core::GetMetric</code> - Provides information about specific device.
  <code>InferenceEngine::Core::GetConfig</code> - Gets the current value of a specific configuration key.
* <code>InferenceEngine::Core::SetConfig</code> - Sets a new value for the configuration key.

The `InferenceEngine::ExecutableNetwork` class is also extended to support the Query API:

* <code>InferenceEngine::ExecutableNetwork::GetMetric</code>
* <code>InferenceEngine::ExecutableNetwork::GetConfig</code>
* <code>InferenceEngine::ExecutableNetwork::SetConfig</code>

## Query API in the Core Class

### GetAvailableDevices

```cpp
InferenceEngine::Core core;
std::vector<std::string> availableDevices = ie.GetAvailableDevices();
```

The function returns list of available devices, for example:
```
MYRIAD.1.2-ma2480
MYRIAD.1.4-ma2480
FPGA.0
FPGA.1
CPU
GPU
...
```

Each device name can then be passed to:

* `InferenceEngine::Core::LoadNetwork` to load the network to a specific device.
* `InferenceEngine::Core::GetMetric` to get common or device specific metrics.
* All other methods of the `Core` class that accept `deviceName`.

### GetConfig()

The code below demonstrates how to understand whether `HETERO` device dumps `.dot` files with split graphs during the split stage:

```cpp
InferenceEngine::Core core;
bool dumpDotFile = core.GetConfig("HETERO", HETERO_CONFIG_KEY(DUMP_GRAPH_DOT)).as<bool>();
```

For documentation about common configuration keys, refer to `ie_plugin_config.hpp`. Device specific configuration keys can be found in corresponding plugin folders.

### GetMetric()

* To extract device properties such as available device, device name, supported configuration keys, and others, use the `InferenceEngine::Core::GetMetric` method:

```cpp
InferenceEngine::Core core;
std::string cpuDeviceName = core.GetMetric("GPU", METRIC_KEY(FULL_DEVICE_NAME)).as<std::string>();
```

A returned value looks as follows: `Intel(R) Core(TM) i7-8700 CPU @ 3.20GHz`.

> **NOTE**: All metrics have specific type, which is specified during metric instantiation. The list of common device-agnostic metrics can be found in `ie_plugin_config.hpp`. Device specific metrics (for example, for `HDDL`, `MYRIAD` devices) can be found in corresponding plugin folders.

## Query API in the ExecutableNetwork Class

### GetMetric()

The method is used to get executable network specific metric such as `METRIC_KEY(OPTIMAL_NUMBER_OF_INFER_REQUESTS)`:
```cpp
InferenceEngine::Core core;
auto exeNetwork = core.LoadNetwork(network, "CPU");
auto nireq = exeNetwork.GetMetric(METRIC_KEY(OPTIMAL_NUMBER_OF_INFER_REQUESTS)).as<unsigned int>();
```

Or the current temperature of `MYRIAD` device:
```cpp
InferenceEngine::Core core;
auto exeNetwork = core.LoadNetwork(network, "MYRIAD");
float temperature = exeNetwork.GetMetric(METRIC_KEY(DEVICE_THERMAL)).as<float>();
```

### GetConfig()

The method is used to get information about configuration values the executable network has been created with:

```cpp
InferenceEngine::Core core;
auto exeNetwork = core.LoadNetwork(network, "CPU");
auto ncores = exeNetwork.GetConfig(PluginConfigParams::KEY_CPU_THREADS_NUM).as<std::string>();
```

### SetConfig()

The only device that supports this method is [Multi-Device](supported_plugins/MULTI.md).
