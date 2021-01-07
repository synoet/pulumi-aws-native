// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Cloudformation.AppMesh.Outputs
{

    [OutputType]
    public sealed class RouteAttributes
    {
        public readonly string Arn;
        public readonly string MeshName;
        public readonly string MeshOwner;
        public readonly string ResourceOwner;
        public readonly string RouteName;
        public readonly string Uid;
        public readonly string VirtualRouterName;

        [OutputConstructor]
        private RouteAttributes(
            string Arn,

            string MeshName,

            string MeshOwner,

            string ResourceOwner,

            string RouteName,

            string Uid,

            string VirtualRouterName)
        {
            this.Arn = Arn;
            this.MeshName = MeshName;
            this.MeshOwner = MeshOwner;
            this.ResourceOwner = ResourceOwner;
            this.RouteName = RouteName;
            this.Uid = Uid;
            this.VirtualRouterName = VirtualRouterName;
        }
    }
}