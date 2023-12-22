// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.SageMaker.Inputs
{

    public sealed class OnlineStoreConfigPropertiesArgs : global::Pulumi.ResourceArgs
    {
        [Input("enableOnlineStore")]
        public Input<bool>? EnableOnlineStore { get; set; }

        [Input("securityConfig")]
        public Input<Inputs.FeatureGroupOnlineStoreSecurityConfigArgs>? SecurityConfig { get; set; }

        [Input("storageType")]
        public Input<Pulumi.AwsNative.SageMaker.FeatureGroupStorageType>? StorageType { get; set; }

        public OnlineStoreConfigPropertiesArgs()
        {
        }
        public static new OnlineStoreConfigPropertiesArgs Empty => new OnlineStoreConfigPropertiesArgs();
    }
}
