// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Batch.Inputs
{

    public sealed class JobDefinitionEksPropertiesArgs : global::Pulumi.ResourceArgs
    {
        [Input("podProperties")]
        public Input<Inputs.JobDefinitionPodPropertiesArgs>? PodProperties { get; set; }

        public JobDefinitionEksPropertiesArgs()
        {
        }
        public static new JobDefinitionEksPropertiesArgs Empty => new JobDefinitionEksPropertiesArgs();
    }
}
