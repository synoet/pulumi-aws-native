// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Glue.Inputs
{

    public sealed class MLTransformInputRecordTablesArgs : global::Pulumi.ResourceArgs
    {
        [Input("glueTables")]
        private InputList<Inputs.MLTransformGlueTablesArgs>? _glueTables;
        public InputList<Inputs.MLTransformGlueTablesArgs> GlueTables
        {
            get => _glueTables ?? (_glueTables = new InputList<Inputs.MLTransformGlueTablesArgs>());
            set => _glueTables = value;
        }

        public MLTransformInputRecordTablesArgs()
        {
        }
        public static new MLTransformInputRecordTablesArgs Empty => new MLTransformInputRecordTablesArgs();
    }
}
