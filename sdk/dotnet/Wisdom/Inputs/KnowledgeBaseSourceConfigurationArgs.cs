// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Wisdom.Inputs
{

    public sealed class KnowledgeBaseSourceConfigurationArgs : global::Pulumi.ResourceArgs
    {
        [Input("appIntegrations")]
        public Input<Inputs.KnowledgeBaseAppIntegrationsConfigurationArgs>? AppIntegrations { get; set; }

        public KnowledgeBaseSourceConfigurationArgs()
        {
        }
        public static new KnowledgeBaseSourceConfigurationArgs Empty => new KnowledgeBaseSourceConfigurationArgs();
    }
}
