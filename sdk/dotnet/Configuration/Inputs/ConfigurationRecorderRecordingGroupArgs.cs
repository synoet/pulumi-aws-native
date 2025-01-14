// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Configuration.Inputs
{

    public sealed class ConfigurationRecorderRecordingGroupArgs : global::Pulumi.ResourceArgs
    {
        [Input("allSupported")]
        public Input<bool>? AllSupported { get; set; }

        [Input("exclusionByResourceTypes")]
        public Input<Inputs.ConfigurationRecorderExclusionByResourceTypesArgs>? ExclusionByResourceTypes { get; set; }

        [Input("includeGlobalResourceTypes")]
        public Input<bool>? IncludeGlobalResourceTypes { get; set; }

        [Input("recordingStrategy")]
        public Input<Inputs.ConfigurationRecorderRecordingStrategyArgs>? RecordingStrategy { get; set; }

        [Input("resourceTypes")]
        private InputList<string>? _resourceTypes;
        public InputList<string> ResourceTypes
        {
            get => _resourceTypes ?? (_resourceTypes = new InputList<string>());
            set => _resourceTypes = value;
        }

        public ConfigurationRecorderRecordingGroupArgs()
        {
        }
        public static new ConfigurationRecorderRecordingGroupArgs Empty => new ConfigurationRecorderRecordingGroupArgs();
    }
}
