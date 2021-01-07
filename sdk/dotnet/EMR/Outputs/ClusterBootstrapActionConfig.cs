// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Cloudformation.EMR.Outputs
{

    [OutputType]
    public sealed class ClusterBootstrapActionConfig
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-bootstrapactionconfig.html#cfn-elasticmapreduce-cluster-bootstrapactionconfig-name
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-bootstrapactionconfig.html#cfn-elasticmapreduce-cluster-bootstrapactionconfig-scriptbootstrapaction
        /// </summary>
        public readonly Outputs.ClusterScriptBootstrapActionConfig ScriptBootstrapAction;

        [OutputConstructor]
        private ClusterBootstrapActionConfig(
            string Name,

            Outputs.ClusterScriptBootstrapActionConfig ScriptBootstrapAction)
        {
            this.Name = Name;
            this.ScriptBootstrapAction = ScriptBootstrapAction;
        }
    }
}