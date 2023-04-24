// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.RAM
{
    public static class GetPermission
    {
        /// <summary>
        /// Resource type definition for AWS::RAM::Permission
        /// </summary>
        public static Task<GetPermissionResult> InvokeAsync(GetPermissionArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetPermissionResult>("aws-native:ram:getPermission", args ?? new GetPermissionArgs(), options.WithDefaults());

        /// <summary>
        /// Resource type definition for AWS::RAM::Permission
        /// </summary>
        public static Output<GetPermissionResult> Invoke(GetPermissionInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetPermissionResult>("aws-native:ram:getPermission", args ?? new GetPermissionInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetPermissionArgs : global::Pulumi.InvokeArgs
    {
        [Input("arn", required: true)]
        public string Arn { get; set; } = null!;

        public GetPermissionArgs()
        {
        }
        public static new GetPermissionArgs Empty => new GetPermissionArgs();
    }

    public sealed class GetPermissionInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("arn", required: true)]
        public Input<string> Arn { get; set; } = null!;

        public GetPermissionInvokeArgs()
        {
        }
        public static new GetPermissionInvokeArgs Empty => new GetPermissionInvokeArgs();
    }


    [OutputType]
    public sealed class GetPermissionResult
    {
        public readonly string? Arn;
        /// <summary>
        /// Set to true to use this as the default permission.
        /// </summary>
        public readonly bool? IsResourceTypeDefault;
        public readonly string? PermissionType;
        public readonly ImmutableArray<Outputs.PermissionTag> Tags;
        /// <summary>
        /// Version of the permission.
        /// </summary>
        public readonly string? Version;

        [OutputConstructor]
        private GetPermissionResult(
            string? arn,

            bool? isResourceTypeDefault,

            string? permissionType,

            ImmutableArray<Outputs.PermissionTag> tags,

            string? version)
        {
            Arn = arn;
            IsResourceTypeDefault = isResourceTypeDefault;
            PermissionType = permissionType;
            Tags = tags;
            Version = version;
        }
    }
}
