// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.IoTFleetWise.Inputs
{

    public sealed class CollectionScheme1PropertiesArgs : global::Pulumi.ResourceArgs
    {
        [Input("conditionBasedCollectionScheme", required: true)]
        public Input<Inputs.CampaignConditionBasedCollectionSchemeArgs> ConditionBasedCollectionScheme { get; set; } = null!;

        public CollectionScheme1PropertiesArgs()
        {
        }
        public static new CollectionScheme1PropertiesArgs Empty => new CollectionScheme1PropertiesArgs();
    }
}
