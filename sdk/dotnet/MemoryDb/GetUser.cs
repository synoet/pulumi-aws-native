// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.MemoryDb
{
    public static class GetUser
    {
        /// <summary>
        /// Resource Type definition for AWS::MemoryDB::User
        /// </summary>
        public static Task<GetUserResult> InvokeAsync(GetUserArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetUserResult>("aws-native:memorydb:getUser", args ?? new GetUserArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::MemoryDB::User
        /// </summary>
        public static Output<GetUserResult> Invoke(GetUserInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetUserResult>("aws-native:memorydb:getUser", args ?? new GetUserInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetUserArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The name of the user.
        /// </summary>
        [Input("userName", required: true)]
        public string UserName { get; set; } = null!;

        public GetUserArgs()
        {
        }
        public static new GetUserArgs Empty => new GetUserArgs();
    }

    public sealed class GetUserInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The name of the user.
        /// </summary>
        [Input("userName", required: true)]
        public Input<string> UserName { get; set; } = null!;

        public GetUserInvokeArgs()
        {
        }
        public static new GetUserInvokeArgs Empty => new GetUserInvokeArgs();
    }


    [OutputType]
    public sealed class GetUserResult
    {
        /// <summary>
        /// The Amazon Resource Name (ARN) of the user account.
        /// </summary>
        public readonly string? Arn;
        /// <summary>
        /// Indicates the user status. Can be "active", "modifying" or "deleting".
        /// </summary>
        public readonly string? Status;
        /// <summary>
        /// An array of key-value pairs to apply to this user.
        /// </summary>
        public readonly ImmutableArray<Outputs.UserTag> Tags;

        [OutputConstructor]
        private GetUserResult(
            string? arn,

            string? status,

            ImmutableArray<Outputs.UserTag> tags)
        {
            Arn = arn;
            Status = status;
            Tags = tags;
        }
    }
}
