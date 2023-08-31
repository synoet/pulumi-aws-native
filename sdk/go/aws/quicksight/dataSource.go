// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package quicksight

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Definition of the AWS::QuickSight::DataSource Resource Type.
type DataSource struct {
	pulumi.CustomResourceState

	// <p>A set of alternate data source parameters that you want to share for the credentials
	//             stored with this data source. The credentials are applied in tandem with the data source
	//             parameters when you copy a data source by using a create or update request. The API
	//             operation compares the <code>DataSourceParameters</code> structure that's in the request
	//             with the structures in the <code>AlternateDataSourceParameters</code> allow list. If the
	//             structures are an exact match, the request is allowed to use the credentials from this
	//             existing data source. If the <code>AlternateDataSourceParameters</code> list is null,
	//             the <code>Credentials</code> originally used with this <code>DataSourceParameters</code>
	//             are automatically allowed.</p>
	AlternateDataSourceParameters DataSourceParametersArrayOutput `pulumi:"alternateDataSourceParameters"`
	// <p>The Amazon Resource Name (ARN) of the data source.</p>
	Arn          pulumi.StringOutput    `pulumi:"arn"`
	AwsAccountId pulumi.StringPtrOutput `pulumi:"awsAccountId"`
	// <p>The time that this data source was created.</p>
	CreatedTime          pulumi.StringOutput            `pulumi:"createdTime"`
	Credentials          DataSourceCredentialsPtrOutput `pulumi:"credentials"`
	DataSourceId         pulumi.StringPtrOutput         `pulumi:"dataSourceId"`
	DataSourceParameters DataSourceParametersPtrOutput  `pulumi:"dataSourceParameters"`
	ErrorInfo            DataSourceErrorInfoPtrOutput   `pulumi:"errorInfo"`
	// <p>The last time that this data source was updated.</p>
	LastUpdatedTime pulumi.StringOutput `pulumi:"lastUpdatedTime"`
	// <p>A display name for the data source.</p>
	Name pulumi.StringPtrOutput `pulumi:"name"`
	// <p>A list of resource permissions on the data source.</p>
	Permissions   DataSourceResourcePermissionArrayOutput `pulumi:"permissions"`
	SslProperties DataSourceSslPropertiesPtrOutput        `pulumi:"sslProperties"`
	Status        DataSourceResourceStatusOutput          `pulumi:"status"`
	// <p>Contains a map of the key-value pairs for the resource tag or tags assigned to the data source.</p>
	Tags                    DataSourceTagArrayOutput                   `pulumi:"tags"`
	Type                    DataSourceTypePtrOutput                    `pulumi:"type"`
	VpcConnectionProperties DataSourceVpcConnectionPropertiesPtrOutput `pulumi:"vpcConnectionProperties"`
}

// NewDataSource registers a new resource with the given unique name, arguments, and options.
func NewDataSource(ctx *pulumi.Context,
	name string, args *DataSourceArgs, opts ...pulumi.ResourceOption) (*DataSource, error) {
	if args == nil {
		args = &DataSourceArgs{}
	}

	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"awsAccountId",
		"dataSourceId",
		"type",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource DataSource
	err := ctx.RegisterResource("aws-native:quicksight:DataSource", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetDataSource gets an existing DataSource resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetDataSource(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *DataSourceState, opts ...pulumi.ResourceOption) (*DataSource, error) {
	var resource DataSource
	err := ctx.ReadResource("aws-native:quicksight:DataSource", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering DataSource resources.
type dataSourceState struct {
}

type DataSourceState struct {
}

func (DataSourceState) ElementType() reflect.Type {
	return reflect.TypeOf((*dataSourceState)(nil)).Elem()
}

type dataSourceArgs struct {
	// <p>A set of alternate data source parameters that you want to share for the credentials
	//             stored with this data source. The credentials are applied in tandem with the data source
	//             parameters when you copy a data source by using a create or update request. The API
	//             operation compares the <code>DataSourceParameters</code> structure that's in the request
	//             with the structures in the <code>AlternateDataSourceParameters</code> allow list. If the
	//             structures are an exact match, the request is allowed to use the credentials from this
	//             existing data source. If the <code>AlternateDataSourceParameters</code> list is null,
	//             the <code>Credentials</code> originally used with this <code>DataSourceParameters</code>
	//             are automatically allowed.</p>
	AlternateDataSourceParameters []DataSourceParameters `pulumi:"alternateDataSourceParameters"`
	AwsAccountId                  *string                `pulumi:"awsAccountId"`
	Credentials                   *DataSourceCredentials `pulumi:"credentials"`
	DataSourceId                  *string                `pulumi:"dataSourceId"`
	DataSourceParameters          *DataSourceParameters  `pulumi:"dataSourceParameters"`
	ErrorInfo                     *DataSourceErrorInfo   `pulumi:"errorInfo"`
	// <p>A display name for the data source.</p>
	Name *string `pulumi:"name"`
	// <p>A list of resource permissions on the data source.</p>
	Permissions   []DataSourceResourcePermission `pulumi:"permissions"`
	SslProperties *DataSourceSslProperties       `pulumi:"sslProperties"`
	// <p>Contains a map of the key-value pairs for the resource tag or tags assigned to the data source.</p>
	Tags                    []DataSourceTag                    `pulumi:"tags"`
	Type                    *DataSourceType                    `pulumi:"type"`
	VpcConnectionProperties *DataSourceVpcConnectionProperties `pulumi:"vpcConnectionProperties"`
}

// The set of arguments for constructing a DataSource resource.
type DataSourceArgs struct {
	// <p>A set of alternate data source parameters that you want to share for the credentials
	//             stored with this data source. The credentials are applied in tandem with the data source
	//             parameters when you copy a data source by using a create or update request. The API
	//             operation compares the <code>DataSourceParameters</code> structure that's in the request
	//             with the structures in the <code>AlternateDataSourceParameters</code> allow list. If the
	//             structures are an exact match, the request is allowed to use the credentials from this
	//             existing data source. If the <code>AlternateDataSourceParameters</code> list is null,
	//             the <code>Credentials</code> originally used with this <code>DataSourceParameters</code>
	//             are automatically allowed.</p>
	AlternateDataSourceParameters DataSourceParametersArrayInput
	AwsAccountId                  pulumi.StringPtrInput
	Credentials                   DataSourceCredentialsPtrInput
	DataSourceId                  pulumi.StringPtrInput
	DataSourceParameters          DataSourceParametersPtrInput
	ErrorInfo                     DataSourceErrorInfoPtrInput
	// <p>A display name for the data source.</p>
	Name pulumi.StringPtrInput
	// <p>A list of resource permissions on the data source.</p>
	Permissions   DataSourceResourcePermissionArrayInput
	SslProperties DataSourceSslPropertiesPtrInput
	// <p>Contains a map of the key-value pairs for the resource tag or tags assigned to the data source.</p>
	Tags                    DataSourceTagArrayInput
	Type                    DataSourceTypePtrInput
	VpcConnectionProperties DataSourceVpcConnectionPropertiesPtrInput
}

func (DataSourceArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*dataSourceArgs)(nil)).Elem()
}

type DataSourceInput interface {
	pulumi.Input

	ToDataSourceOutput() DataSourceOutput
	ToDataSourceOutputWithContext(ctx context.Context) DataSourceOutput
}

func (*DataSource) ElementType() reflect.Type {
	return reflect.TypeOf((**DataSource)(nil)).Elem()
}

func (i *DataSource) ToDataSourceOutput() DataSourceOutput {
	return i.ToDataSourceOutputWithContext(context.Background())
}

func (i *DataSource) ToDataSourceOutputWithContext(ctx context.Context) DataSourceOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DataSourceOutput)
}

type DataSourceOutput struct{ *pulumi.OutputState }

func (DataSourceOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**DataSource)(nil)).Elem()
}

func (o DataSourceOutput) ToDataSourceOutput() DataSourceOutput {
	return o
}

func (o DataSourceOutput) ToDataSourceOutputWithContext(ctx context.Context) DataSourceOutput {
	return o
}

// <p>A set of alternate data source parameters that you want to share for the credentials
//
//	stored with this data source. The credentials are applied in tandem with the data source
//	parameters when you copy a data source by using a create or update request. The API
//	operation compares the <code>DataSourceParameters</code> structure that's in the request
//	with the structures in the <code>AlternateDataSourceParameters</code> allow list. If the
//	structures are an exact match, the request is allowed to use the credentials from this
//	existing data source. If the <code>AlternateDataSourceParameters</code> list is null,
//	the <code>Credentials</code> originally used with this <code>DataSourceParameters</code>
//	are automatically allowed.</p>
func (o DataSourceOutput) AlternateDataSourceParameters() DataSourceParametersArrayOutput {
	return o.ApplyT(func(v *DataSource) DataSourceParametersArrayOutput { return v.AlternateDataSourceParameters }).(DataSourceParametersArrayOutput)
}

// <p>The Amazon Resource Name (ARN) of the data source.</p>
func (o DataSourceOutput) Arn() pulumi.StringOutput {
	return o.ApplyT(func(v *DataSource) pulumi.StringOutput { return v.Arn }).(pulumi.StringOutput)
}

func (o DataSourceOutput) AwsAccountId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *DataSource) pulumi.StringPtrOutput { return v.AwsAccountId }).(pulumi.StringPtrOutput)
}

// <p>The time that this data source was created.</p>
func (o DataSourceOutput) CreatedTime() pulumi.StringOutput {
	return o.ApplyT(func(v *DataSource) pulumi.StringOutput { return v.CreatedTime }).(pulumi.StringOutput)
}

func (o DataSourceOutput) Credentials() DataSourceCredentialsPtrOutput {
	return o.ApplyT(func(v *DataSource) DataSourceCredentialsPtrOutput { return v.Credentials }).(DataSourceCredentialsPtrOutput)
}

func (o DataSourceOutput) DataSourceId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *DataSource) pulumi.StringPtrOutput { return v.DataSourceId }).(pulumi.StringPtrOutput)
}

func (o DataSourceOutput) DataSourceParameters() DataSourceParametersPtrOutput {
	return o.ApplyT(func(v *DataSource) DataSourceParametersPtrOutput { return v.DataSourceParameters }).(DataSourceParametersPtrOutput)
}

func (o DataSourceOutput) ErrorInfo() DataSourceErrorInfoPtrOutput {
	return o.ApplyT(func(v *DataSource) DataSourceErrorInfoPtrOutput { return v.ErrorInfo }).(DataSourceErrorInfoPtrOutput)
}

// <p>The last time that this data source was updated.</p>
func (o DataSourceOutput) LastUpdatedTime() pulumi.StringOutput {
	return o.ApplyT(func(v *DataSource) pulumi.StringOutput { return v.LastUpdatedTime }).(pulumi.StringOutput)
}

// <p>A display name for the data source.</p>
func (o DataSourceOutput) Name() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *DataSource) pulumi.StringPtrOutput { return v.Name }).(pulumi.StringPtrOutput)
}

// <p>A list of resource permissions on the data source.</p>
func (o DataSourceOutput) Permissions() DataSourceResourcePermissionArrayOutput {
	return o.ApplyT(func(v *DataSource) DataSourceResourcePermissionArrayOutput { return v.Permissions }).(DataSourceResourcePermissionArrayOutput)
}

func (o DataSourceOutput) SslProperties() DataSourceSslPropertiesPtrOutput {
	return o.ApplyT(func(v *DataSource) DataSourceSslPropertiesPtrOutput { return v.SslProperties }).(DataSourceSslPropertiesPtrOutput)
}

func (o DataSourceOutput) Status() DataSourceResourceStatusOutput {
	return o.ApplyT(func(v *DataSource) DataSourceResourceStatusOutput { return v.Status }).(DataSourceResourceStatusOutput)
}

// <p>Contains a map of the key-value pairs for the resource tag or tags assigned to the data source.</p>
func (o DataSourceOutput) Tags() DataSourceTagArrayOutput {
	return o.ApplyT(func(v *DataSource) DataSourceTagArrayOutput { return v.Tags }).(DataSourceTagArrayOutput)
}

func (o DataSourceOutput) Type() DataSourceTypePtrOutput {
	return o.ApplyT(func(v *DataSource) DataSourceTypePtrOutput { return v.Type }).(DataSourceTypePtrOutput)
}

func (o DataSourceOutput) VpcConnectionProperties() DataSourceVpcConnectionPropertiesPtrOutput {
	return o.ApplyT(func(v *DataSource) DataSourceVpcConnectionPropertiesPtrOutput { return v.VpcConnectionProperties }).(DataSourceVpcConnectionPropertiesPtrOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*DataSourceInput)(nil)).Elem(), &DataSource{})
	pulumi.RegisterOutputType(DataSourceOutput{})
}
