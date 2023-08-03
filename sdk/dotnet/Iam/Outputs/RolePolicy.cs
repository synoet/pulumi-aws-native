// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Iam.Outputs
{

    /// <summary>
    /// The inline policy document that is embedded in the specified IAM role.
    /// </summary>
    [OutputType]
    public sealed class RolePolicy
    {
        /// <summary>
        /// The policy document.
        /// </summary>
        public readonly string PolicyDocument;
        /// <summary>
        /// The friendly name (not ARN) identifying the policy.
        /// </summary>
        public readonly string PolicyName;

        [OutputConstructor]
        private RolePolicy(
            string policyDocument,

            string policyName)
        {
            PolicyDocument = policyDocument;
            PolicyName = policyName;
        }
    }
}
