// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Cloudformation.IAM.Inputs
{

    /// <summary>
    /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html
    /// </summary>
    public sealed class RolePropertiesArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html#cfn-iam-role-assumerolepolicydocument
        /// </summary>
        [Input("AssumeRolePolicyDocument", required: true)]
        public InputUnion<System.Text.Json.JsonElement, string> AssumeRolePolicyDocument { get; set; } = null!;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html#cfn-iam-role-description
        /// </summary>
        [Input("Description")]
        public Input<string>? Description { get; set; }

        [Input("ManagedPolicyArns")]
        private InputList<string>? _ManagedPolicyArns;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html#cfn-iam-role-managepolicyarns
        /// </summary>
        public InputList<string> ManagedPolicyArns
        {
            get => _ManagedPolicyArns ?? (_ManagedPolicyArns = new InputList<string>());
            set => _ManagedPolicyArns = value;
        }

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html#cfn-iam-role-maxsessionduration
        /// </summary>
        [Input("MaxSessionDuration")]
        public Input<int>? MaxSessionDuration { get; set; }

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html#cfn-iam-role-path
        /// </summary>
        [Input("Path")]
        public Input<string>? Path { get; set; }

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html#cfn-iam-role-permissionsboundary
        /// </summary>
        [Input("PermissionsBoundary")]
        public Input<string>? PermissionsBoundary { get; set; }

        [Input("Policies")]
        private InputList<Inputs.RolePolicyArgs>? _Policies;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html#cfn-iam-role-policies
        /// </summary>
        public InputList<Inputs.RolePolicyArgs> Policies
        {
            get => _Policies ?? (_Policies = new InputList<Inputs.RolePolicyArgs>());
            set => _Policies = value;
        }

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html#cfn-iam-role-rolename
        /// </summary>
        [Input("RoleName")]
        public Input<string>? RoleName { get; set; }

        [Input("Tags")]
        private InputList<Pulumi.Cloudformation.Inputs.TagArgs>? _Tags;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html#cfn-iam-role-tags
        /// </summary>
        public InputList<Pulumi.Cloudformation.Inputs.TagArgs> Tags
        {
            get => _Tags ?? (_Tags = new InputList<Pulumi.Cloudformation.Inputs.TagArgs>());
            set => _Tags = value;
        }

        public RolePropertiesArgs()
        {
        }
    }
}