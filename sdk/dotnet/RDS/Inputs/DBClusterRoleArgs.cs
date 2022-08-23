// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.RDS.Inputs
{

    /// <summary>
    /// Describes an AWS Identity and Access Management (IAM) role that is associated with a DB cluster.
    /// </summary>
    public sealed class DBClusterRoleArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The name of the feature associated with the AWS Identity and Access Management (IAM) role. For the list of supported feature names, see DBEngineVersion in the Amazon RDS API Reference.
        /// </summary>
        [Input("featureName")]
        public Input<string>? FeatureName { get; set; }

        /// <summary>
        /// The Amazon Resource Name (ARN) of the IAM role that is associated with the DB cluster.
        /// </summary>
        [Input("roleArn", required: true)]
        public Input<string> RoleArn { get; set; } = null!;

        public DBClusterRoleArgs()
        {
        }
        public static new DBClusterRoleArgs Empty => new DBClusterRoleArgs();
    }
}
