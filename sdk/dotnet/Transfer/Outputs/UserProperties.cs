// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Cloudformation.Transfer.Outputs
{

    [OutputType]
    public sealed class UserProperties
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-user.html#cfn-transfer-user-homedirectory
        /// </summary>
        public readonly string? HomeDirectory;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-user.html#cfn-transfer-user-homedirectorymappings
        /// </summary>
        public readonly ImmutableArray<Outputs.UserHomeDirectoryMapEntry> HomeDirectoryMappings;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-user.html#cfn-transfer-user-homedirectorytype
        /// </summary>
        public readonly string? HomeDirectoryType;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-user.html#cfn-transfer-user-policy
        /// </summary>
        public readonly string? Policy;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-user.html#cfn-transfer-user-role
        /// </summary>
        public readonly string Role;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-user.html#cfn-transfer-user-serverid
        /// </summary>
        public readonly string ServerId;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-user.html#cfn-transfer-user-sshpublickeys
        /// </summary>
        public readonly ImmutableArray<Outputs.UserSshPublicKey> SshPublicKeys;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-user.html#cfn-transfer-user-tags
        /// </summary>
        public readonly ImmutableArray<Pulumi.Cloudformation.Outputs.Tag> Tags;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-user.html#cfn-transfer-user-username
        /// </summary>
        public readonly string UserName;

        [OutputConstructor]
        private UserProperties(
            string? HomeDirectory,

            ImmutableArray<Outputs.UserHomeDirectoryMapEntry> HomeDirectoryMappings,

            string? HomeDirectoryType,

            string? Policy,

            string Role,

            string ServerId,

            ImmutableArray<Outputs.UserSshPublicKey> SshPublicKeys,

            ImmutableArray<Pulumi.Cloudformation.Outputs.Tag> Tags,

            string UserName)
        {
            this.HomeDirectory = HomeDirectory;
            this.HomeDirectoryMappings = HomeDirectoryMappings;
            this.HomeDirectoryType = HomeDirectoryType;
            this.Policy = Policy;
            this.Role = Role;
            this.ServerId = ServerId;
            this.SshPublicKeys = SshPublicKeys;
            this.Tags = Tags;
            this.UserName = UserName;
        }
    }
}